### GET@Path
#### Server: Response
`script.py`
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/src/{param00}")
def response(param00: str):
    serverResponse = dict()
    serverResponse["rspns00"] = "Alice"
    serverResponse["rspns01"] = 30
    return serverResponse
```
```bash
$ uvicorn script:app --host 0.0.0.0 --port 8000 --reload
```

#### Client: Request

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

data class ServerResponse(
    val rspns00: String,
    val rspns01: Int
)

interface ApiService {
    @GET("/src/{param00}")
    suspend fun request(@Path("param00") param00: String): ServerResponse
}

val retrofit = Retrofit.Builder()
    .baseUrl("http://localhost:8000")
    .addConverterFactory(GsonConverterFactory.create())
    .build()

val api = retrofit.create(ApiService::class.java)

fun main() = runBlocking {
    try {
        api.request("Dao")
    } catch (e: Exception) {
        e.printStackTrace()
        println("${e.message}")
    }
}

main()
```

### GET@Query

#### Server: Response
`script.py`
```python
from fastapi import FastAPI, Path, Query, Request, Body, Header, Cookie, Form, File, UploadFile
from pydantic import BaseModel
from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get("/src")
def response(param00: str, param01: int = 0):
    serverResponse = dict()
    serverResponse["rspns00"] = param00
    serverResponse["rspns01"] = param01
    return serverResponse
```
```bash
$ uvicorn script:app --host 0.0.0.0 --port 8000 --reload
```

#### Client: Request

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

data class ServerResponse(
    val rspns00: String,
    val rspns01: Int
)

interface ApiService {
    @GET("/src")
    suspend fun request(@Query("param00") param00: String, @Query("param01") param01: Int): ServerResponse
}

val retrofit = Retrofit.Builder()
    .baseUrl("http://localhost:8000")
    .addConverterFactory(GsonConverterFactory.create())
    .build()

val api = retrofit.create(ApiService::class.java)

fun main() = runBlocking {
    try {
        api.request("Dao", 20)
    } catch (e: Exception) {
        e.printStackTrace()
        println("${e.message}")
    }
}

main()
```

