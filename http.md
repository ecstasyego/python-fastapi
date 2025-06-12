

## Server: Response
`script.py`
```python
from fastapi import FastAPI
from pydantic import BaseModel

class ClientRequest(BaseModel):
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
def response(param00: ClientRequest):
    serverResponse = dict()
    serverResponse["rspns00"] = "User created"
    serverResponse["rspns01"] = param00
    return serverResponse

@app.put("/src/{param00}")
def response(param00: str, param01: ClientRequest):
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
