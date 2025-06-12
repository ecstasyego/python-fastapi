
## Server: Response
`script.py`
```python
from fastapi import FastAPI
from pydantic import BaseModel

class Response(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.get("/users/{username}")
def get_user(username: str):
    return {"name": "Alice", "age": 30}
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
```
