`authentification.py`
```python
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = "your_secret_key_here" 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password) # Hashed Password: Bcrypt + Salt + Hash

def create_jwt_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) # JWT: HEADER.PAYLOAD.SIGNATURE

def decode_jwt_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) # JWT: HEADER.PAYLOAD.SIGNATURE
    except JWTError:
        return None
```

`script.py`
```python
import bcrypt
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from authentification import verify_password, create_jwt_token, decode_jwt_token

# JWT
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_users_db = {
    "testuser": {
        "username": "testuser",
        "full_name": "Test User",
        "hashed_password": bcrypt.hashpw("secret".encode('utf-8'), bcrypt.gensalt()),  # Hashed Password: Bcrypt + Salt + Hash
    }
}

# API
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # note: distribution-limit
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token = create_jwt_token(data={"sub": user["username"]}) # JWT: HEADER.PAYLOAD.SIGNATURE
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    payload = decode_jwt_token(token) # JWT: HEADER.PAYLOAD.SIGNATURE
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    username = payload.get("sub")
    user = fake_users_db.get(username)
    return user
```

`Server`
```bash
$ PYTHONPATH=/home/[user]/anaconda3/lib/python3.12/site-packages gunicorn -k uvicorn.workers.UvicornWorker script:app --bind 0.0.0.0:8000 --workers 8 --access-logfile -
```

`Client: Curl`
```bash
$ curl -X POST "http://localhost:8000/token" -H "Content-Type: application/x-www-form-urlencoded" -d "username=testuser&password=secret"
$ curl -X GET http://localhost:8000/users/me -H "Authorization: Bearer [JWT]"
```

`Client: Retorift2`
```kts
USE {
    repositories {
        mavenCentral()
    }
    dependencies {
        implementation("com.squareup.retrofit2:retrofit:2.9.0")
        implementation("com.squareup.retrofit2:converter-gson:2.9.0")
        implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.7.3")
    }
}
```
```kts
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.*
import kotlinx.coroutines.runBlocking
import com.google.gson.annotations.SerializedName

data class TokenResponse(
    @SerializedName("access_token") val token: String,
    @SerializedName("token_type") val type: String
)

data class UserResponse(
    @SerializedName("username") val username: String,
    @SerializedName("full_name") val fullName: String? = null
)

interface ApiService {
    @FormUrlEncoded
    @POST("/token")
    suspend fun login(
        @Field("username") username: String,
        @Field("password") password: String
    ): TokenResponse

    @GET("/users/me")
    suspend fun getUserInfo(
        @Header("Authorization") authHeader: String
    ): UserResponse
}

val retrofit = Retrofit.Builder()
    .baseUrl("---.---.---.---") 
    .addConverterFactory(GsonConverterFactory.create())
    .build()

val api = retrofit.create(ApiService::class.java)

fun main() = runBlocking {
    try {
        val loginResponse = api.login("testuser", "secret")
        println("Access Token: ${loginResponse.token}")

        val authHeader = "Bearer ${loginResponse.token}"
        val user = api.getUserInfo(authHeader)
        println("User: ${user.username}")
    } catch (e: Exception) {
        e.printStackTrace()
    }
}

main()
```

`Client: Retorift2 + Okhttp3`
```kts
USE {
    repositories {
        mavenCentral()
    }
    dependencies {
        implementation("com.squareup.retrofit2:retrofit:2.9.0")
        implementation("com.squareup.retrofit2:converter-gson:2.9.0")
        implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.7.3")
        implementation("com.squareup.okhttp3:okhttp:4.11.0")
    }
}
```
```kts
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.*
import kotlinx.coroutines.runBlocking
import com.google.gson.annotations.SerializedName
import okhttp3.Interceptor
import okhttp3.Response
import okhttp3.OkHttpClient


data class TokenResponse(
    @SerializedName("access_token") val token: String,
    @SerializedName("token_type") val type: String
)

data class UserResponse(
    @SerializedName("username") val username: String,
    @SerializedName("full_name") val fullName: String? = null
)

interface ApiService {
    @FormUrlEncoded
    @POST("/token")
    suspend fun login(
        @Field("username") username: String,
        @Field("password") password: String
    ): TokenResponse

    @GET("/users/me")
    suspend fun getUserInfo(): UserResponse
}

class AuthInterceptor(private val tokenProvider: () -> String?) : Interceptor {
    override fun intercept(chain: Interceptor.Chain): Response {
        val requestBuilder = chain.request().newBuilder()
        val token = tokenProvider()
        if (!token.isNullOrEmpty()) {
            requestBuilder.addHeader("Authorization", "Bearer $token")
        }
        return chain.proceed(requestBuilder.build())
    }
}

var accessToken: String? = null

val retrofit = Retrofit.Builder()
    .baseUrl("---.---.---.---")
    .client(OkHttpClient.Builder().addInterceptor(AuthInterceptor { accessToken }).build())
    .addConverterFactory(GsonConverterFactory.create())
    .build()

val api = retrofit.create(ApiService::class.java)

fun main() = runBlocking {
    try {
        val loginResponse = api.login("testuser", "secret")
        accessToken = loginResponse.token
        println("Access Token: $accessToken")

        val user = api.getUserInfo()
        println("User: ${user.username}")
    } catch (e: Exception) {
        e.printStackTrace()
    }
}

main()
```
