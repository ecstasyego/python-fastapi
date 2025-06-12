# python-fastapi 
- ASGI(Asynchronous Server Gateway Interface)
    - FastAPI + [Uvicorn|Hypercorn|Daphne]
    - FastAPI + [Uvicorn|Hypercorn|Daphne] + Gunicorn(Mutli-Threading)
    - FastAPI + [Uvicorn|Hypercorn|Daphne] + Gunicorn(Mutli-Threading) + Nginx(Reverse Proxy)
    - FastAPI + [Uvicorn|Hypercorn|Daphne] + Gunicorn(Mutli-Threading) + Nginx(Reverse Proxy) + CDN(Clouded Cache)
    - FastAPI + [Uvicorn|Hypercorn|Daphne] + Gunicorn(Mutli-Threading) + Nginx(Reverse Proxy) + CDN(Clouded Cache) + OpenVPN(Security)

`Installation`
```bash
$ pip install fastapi
$ pip install uvicorn
```
`Installation: JWT`
```bash
$ pip install python-jose[cryptography] 
$ pip install passlib[bcrypt]
$ pip install python-multipart
```


## Server-Side: Response
`script.py`
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, FastAPI!"}
```

`Server: Development`
```bash
$ uvicorn script:app --reload
```

`Server: Production`
```bash
$ uvicorn script:app
$ uvicorn script:app --host 0.0.0.0 --port 8000
$ uvicorn script:app --host 0.0.0.0 --port 8000 --workers 4
```
```bash
$ gunicorn -k uvicorn.workers.UvicornWorker script:app
$ gunicorn -k uvicorn.workers.UvicornWorker script:app -b 0.0.0.0:8000
$ gunicorn -k uvicorn.workers.UvicornWorker script:app -b 0.0.0.0:8000 -w 4
$ gunicorn -k uvicorn.workers.UvicornWorker script:app --bind 0.0.0.0:8000 --workers 4
$ gunicorn -k uvicorn.workers.UvicornWorker script:app --bind 0.0.0.0:8000 --workers 4 --access-logfile -
```
```bash
$ which python
$ which pip
$ which uvicorn
$ which gunicorn
$ PYTHONPATH=/home/[user]/anaconda3/lib/python3.12/site-packages gunicorn -k uvicorn.workers.UvicornWorker script:app
$ PYTHONPATH=/home/[user]/anaconda3/lib/python3.12/site-packages gunicorn -k uvicorn.workers.UvicornWorker script:app -b 0.0.0.0:8000
$ PYTHONPATH=/home/[user]/anaconda3/lib/python3.12/site-packages gunicorn -k uvicorn.workers.UvicornWorker script:app -b 0.0.0.0:8000 -w 4
$ PYTHONPATH=/home/[user]/anaconda3/lib/python3.12/site-packages gunicorn -k uvicorn.workers.UvicornWorker script:app --bind 0.0.0.0:8000 --workers 4
$ PYTHONPATH=/home/[user]/anaconda3/lib/python3.12/site-packages gunicorn -k uvicorn.workers.UvicornWorker script:app --bind 0.0.0.0:8000 --workers 4 --access-logfile -
```

## Client-Side: Request

`Bash: Curl`
```bash
$ curl http://127.0.0.1:8000
$ curl http://127.0.0.1:8000/docs
```


<br><br><br>

# Examples
## Json API
### Server: Response
`script.py`
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, FastAPI!"}
```
```bash
$ uvicorn main:app --reload
$ uvicorn main:app --host 0.0.0.0 --reload
$ uvicorn main:app --port 8000 --reload
$ uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```


### Client: Request
`Kotlin: Retrofit`
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
import retrofit2.http.GET
import kotlinx.coroutines.runBlocking
import com.google.gson.annotations.SerializedName

data class Response(
    @SerializedName("message") val message: String
)

interface ApiService {
    @GET("/")
    suspend fun getData(): Response
}

val retrofit = Retrofit.Builder()
    .baseUrl("http://localhost:8000")
    .addConverterFactory(GsonConverterFactory.create())
    .build()

val api = retrofit.create(ApiService::class.java)

fun main() = runBlocking {
    try {
        api.getData()
    } catch (e: Exception) {
        e.printStackTrace()
    }
}

main()
```


## DataFrame API
### Server: Response

`main.py`
```python
import numpy as np
import pandas as pd
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    df = pd.DataFrame(data=np.random.normal(size=(30, 5)), columns=list('ABCDE'))
    df = df.astype(object)
    df = df.where(pd.notnull(df), None).replace([np.inf, -np.inf], None)
    return df.to_dict(orient="records")
```
```bash
$ uvicorn main:app --reload
$ uvicorn main:app --host 0.0.0.0 --reload
$ uvicorn main:app --port 8000 --reload
$ uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Client: Request
`Kotlin: Retrofit2`
```kts
USE {
    repositories {
        mavenCentral()
    }
    dependencies {
        implementation("com.squareup.retrofit2:retrofit:2.9.0")
        implementation("com.squareup.retrofit2:converter-gson:2.9.0")
        implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.7.3")
        implementation("com.google.code.gson:gson:2.10.1")
        implementation("org.jetbrains.kotlinx:dataframe:0.8.0")
    }
}
```
```kts
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.GET
import kotlinx.coroutines.runBlocking
import com.google.gson.annotations.SerializedName

data class Response(
    @SerializedName("A") val col00: Double?,
    @SerializedName("B") val col01: Double?,
    @SerializedName("C") val col02: Double?,
    @SerializedName("D") val col03: Double?,
    @SerializedName("E") val col04: Double?
)

interface ApiService {
    @GET("/")
    suspend fun getData(): List<Response>
}

val retrofit = Retrofit.Builder()
    .baseUrl("http://localhost:8000")
    .addConverterFactory(GsonConverterFactory.create())
    .build()

val api = retrofit.create(ApiService::class.java)

fun main() = runBlocking {
    try {
        api.getData().toDataFrame()
    } catch (e: Exception) {
        e.printStackTrace()
    }
}

main()
```



## HTML API
### Server: Response
`script.py`
```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def index():
    return HTMLResponse("""
        <p>Hello, FastAPI!</p>
    """)
```
```bash
$ uvicorn main:app --reload
$ uvicorn main:app --host 0.0.0.0 --reload
$ uvicorn main:app --port 8000 --reload
$ uvicorn main:app --host 0.0.0.0 --port 8000 --reload
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
import retrofit2.http.GET
import kotlinx.coroutines.runBlocking

interface ApiService {
    @GET("/")
    suspend fun getData(): String
}

val retrofit = Retrofit.Builder()
    .baseUrl("http://localhost:8000")
    .addConverterFactory(ScalarsConverterFactory.create())
    .build()

val api = retrofit.create(ApiService::class.java)

fun main() = runBlocking {
    try {
        api.getData()
    } catch (e: Exception) {
        e.printStackTrace()
    }
}

main()
```


<br><br><br>


