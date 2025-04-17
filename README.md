# python-fastapi
```bash
$ pip install fastapi uvicorn
```

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
```


<br>

## ASGI(Asynchronous Server Gateway Interface)
### FastAPI + [Uvicorn|Hypercorn|Daphne]
### FastAPI + [Uvicorn|Hypercorn|Daphne] + Gunicorn(Mutli-Threading)
### FastAPI + [Uvicorn|Hypercorn|Daphne] + Gunicorn(Mutli-Threading) + Nginx(Reverse Proxy)
### FastAPI + [Uvicorn|Hypercorn|Daphne] + Gunicorn(Mutli-Threading) + Nginx(Reverse Proxy) + CDN(Clouded Cache)
### FastAPI + [Uvicorn|Hypercorn|Daphne] + Gunicorn(Mutli-Threading) + Nginx(Reverse Proxy) + CDN(Clouded Cache) + OpenVPN(Security)





