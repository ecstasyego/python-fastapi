
## Server: Response
`script.py`
```python
from fastapi import FastAPI
from pydantic import BaseModel

class ClientRequest(BaseModel):
    rqst00: str
    rqst01: int

app = FastAPI()

@app.post("/src")
def response(request: ClientRequest):
    serverResponse = dict()
    serverResponse["rspns00"] = "User created"
    serverResponse["rspns01"] = request
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

data class ServerResponse(
    val rspns00: String,
    val rspns01: Request
)

interface ApiService {
    @POST("/src")
    suspend fun getData(@Body rspns01: Request): ServerResponse
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
