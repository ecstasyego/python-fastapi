
## HTTP Method
### Server: Response
`script.py`
```python
from fastapi import FastAPI
from pydantic import BaseModel

class ClientRequestBody(BaseModel):
    rqst00: str
    rqst01: int

app = FastAPI()

@app.get("/src/{param00}")
def response(param00: str):
    serverResponse = dict()
    serverResponse["rspns00"] = "Alice"
    serverResponse["rspns01"] = 30
    return serverResponse

@app.post("/src")
def response(param00: ClientRequestBody):
    serverResponse = dict()
    serverResponse["rspns00"] = "User created"
    serverResponse["rspns01"] = param00
    return serverResponse

@app.put("/src/{param00}")
def response(param00: str, param01: ClientRequestBody):
    serverResponse = dict()
    serverResponse["rspns00"] = "User created"
    serverResponse["rspns01"] = param01
    return serverResponse

@app.patch("/src/{param00}")
def response(param00: str, param01: dict):
    serverResponse = dict()
    serverResponse["rspns00"] = "User created"
    serverResponse["rspns01"] = param01
    return serverResponse

@app.delete("/src/{param00}")
def response(param00: str):
    serverResponse = dict()
    serverResponse["rspns00"] = "User created"
    return serverResponse
```
```bash
$ uvicorn script:app --host 0.0.0.0 --port 8000 --reload
```

### Client: Request

```kts
USE {
    repositories {
        mavenCentral()
    }
    dependencies {
        implementation("com.squareup.retrofit2:retrofit:2.9.0")
        implementation("com.squareup.retrofit2:converter-gson:2.9.0")
        implementation("com.squareup.retrofit2:converter-scalars:2.9.0")
        implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.7.3")
    }
}
```
```kts
import retrofit2.Retrofit
import retrofit2.converter.scalars.ScalarsConverterFactory
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.*
import kotlinx.coroutines.runBlocking

data class Request(
    val rqst00: String,
    val rqst01: Int
)

interface ApiService {
    @GET("/src/{param00}")
    suspend fun getData(@Path("param00") param00: String): Map<String, Any>

    @POST("/src")
    suspend fun postData(@Body param00: Request): Map<String, Any>
    
    @PUT("/src/{param00}")
    suspend fun putData(@Path("param00") param00: String, @Body param01: Request): Map<String, Any>

    @PATCH("/src/{param00}")
    suspend fun patchData(@Path("param00") param00: String, @Body param01: Map<String, @JvmSuppressWildcards Any>): Map<String, Any>

    @DELETE("/src/{param00}")
    suspend fun deleteData(@Path("param00") param00: String): Map<String, Any>
}

val retrofit = Retrofit.Builder()
    .baseUrl("http://localhost:8000")
    .addConverterFactory(GsonConverterFactory.create())
    .build()

val api = retrofit.create(ApiService::class.java)

fun main() = runBlocking {
    try {
        api.getData("Toy")
        api.postData(Request("Bob", 25))
        api.putData("Toy", Request("Bob", 25))
        api.patchData("Toy", mapOf("Bob" to 25))
        api.deleteData("Toy")
        
    } catch (e: Exception) {
        e.printStackTrace()
        println("${e.message}")
    }
}

main()
```


## Content-Type: application/json
### Server: Response
- Parameter
    - Request Components 
        - = Path(...) / = Path(None)
        - = Query(...) / = Query(None)
        - = Body(...) / = Body(None)
        - = Header(...) / = Header(None)
    - Data Types
        - :str / :Optional[str] = None
        - :int / :Optional[int] = None
        - :float / :Optional[float] = None
        - :bool / :Optional[bool] = None

```python
from fastapi import FastAPI, Path, Query, Body, Header
from pydantic import BaseModel
from typing import Optional

class JsonContentType(BaseModel):
    rqst00: str
    rqst01: int
    rqst02: float
    rqst03: bool

    rqst04: Optional[str] = None   # nullable
    rqst05: Optional[int] = None   # nullable
    rqst06: Optional[float] = None # nullable
    rqst07: Optional[bool] = None  # nullable

app = FastAPI()

@app.post("/src/{param00}/{param01}")
def response(
        param00: str = Path(...),
        param01: str = Path(...),
        param02: str = Header(...),
        param03: JsonContentType = Body(...),
        param04: str = Query(...),
        param05: int = Query(...),
        param06: Optional[str] = Query(None),
        param07: Optional[int] = Query(None)
        ):
    serverResponse = dict()
    serverResponse["rspns00"] = "Alice"
    serverResponse["rspns01"] = param03
    return serverResponse
```
```bash
$ uvicorn script:app --host 0.0.0.0 --port 8000 --reload
```

### Client: Request
```kts
USE {
    repositories {
        mavenCentral()
    }
    dependencies {
        implementation("com.squareup.retrofit2:retrofit:2.9.0")
        implementation("com.squareup.retrofit2:converter-gson:2.9.0")
        implementation("com.squareup.retrofit2:converter-scalars:2.9.0")
        implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.7.3")
    }
}
```
```kts
import retrofit2.Retrofit
import retrofit2.converter.scalars.ScalarsConverterFactory
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.*
import kotlinx.coroutines.runBlocking

data class JsonContentType(
    val rqst00: String,
    val rqst01: Int,    
    val rqst02: Float,
    val rqst03: Boolean,    
    
    val rqst04: String?,
    val rqst05: Int?,    
    val rqst06: Float?,
    val rqst07: Boolean?,    
)

interface ApiService {
    @POST("/src/{param00}/{param01}")
    suspend fun request(
        @Path("param00") param00: String, 
        @Path("param01") param01: String,
        @Header("param02") param02: String,
        @Body param03: JsonContentType,
        @Query("param04") param04: String,
        @Query("param05") param05: Int,
        @Query("param06") param06: String?,
        @Query("param07") param07: Int?,        
    ): Map<String, Any>
}

val retrofit = Retrofit.Builder()
    .baseUrl("http://localhost:8000")
    .addConverterFactory(GsonConverterFactory.create())
    .build()

val api = retrofit.create(ApiService::class.java)

fun main() = runBlocking {
    try {
        api.request(
            param00 = "req",
            param01 = "res",
            param02 = "Authentification",
            param03 = JsonContentType(
                rqst00 = "A",
                rqst01 = 1,
                rqst02 = 3.14f,
                rqst03 = true,
                rqst04 = null,
                rqst05 = null,
                rqst06 = null,
                rqst07 = null
            ),
            param04 = "querystring",
            param05 = 1,
            param06 = null,
            param07 = null
        )
    } catch (e: Exception) {
        e.printStackTrace()
        println("${e.message}")
    }
}

main()
```

