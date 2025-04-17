# python-fastapi
`Installation`
```bash
$ pip install fastapi uvicorn
```

### Server

`main.py`
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

### Client
```bash
$ curl http://127.0.0.1:8000
$ curl http://127.0.0.1:8000/docs
```


<br>

## ASGI(Asynchronous Server Gateway Interface)
### FastAPI + [Uvicorn|Hypercorn|Daphne]
### FastAPI + [Uvicorn|Hypercorn|Daphne] + Gunicorn(Mutli-Threading)
### FastAPI + [Uvicorn|Hypercorn|Daphne] + Gunicorn(Mutli-Threading) + Nginx(Reverse Proxy)
### FastAPI + [Uvicorn|Hypercorn|Daphne] + Gunicorn(Mutli-Threading) + Nginx(Reverse Proxy) + CDN(Clouded Cache)
### FastAPI + [Uvicorn|Hypercorn|Daphne] + Gunicorn(Mutli-Threading) + Nginx(Reverse Proxy) + CDN(Clouded Cache) + OpenVPN(Security)





