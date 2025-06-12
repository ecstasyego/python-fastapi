
## Server: Response
`script.py`
```python
from fastapi import FastAPI
from pydantic import BaseModel

class Response(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.post("/users")
def response(request: Response):
    return {"message": "User created", "user": request}
```
```bash
$ uvicorn script:app --host 0.0.0.0 --port 8000 --reload
```

## Client: Request

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
    val name: String,
    val age: Int
)

data class Response(
    val message: String,
    val user: Request
)

interface ApiService {
    @POST("/users")
    suspend fun getData(@Body user: Request): Response
}

val retrofit = Retrofit.Builder()
    .baseUrl("http://localhost:8000")
    .addConverterFactory(GsonConverterFactory.create())
    .build()

val api = retrofit.create(ApiService::class.java)

fun main() = runBlocking {
    try {
        api.getData(Request("Bob", 25))
    } catch (e: Exception) {
        e.printStackTrace()
    }
}

main()
```
