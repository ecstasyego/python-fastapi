# python-fastapi
`Installation`
```bash
$ pip install fastapi
$ pip install uvicorn
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
- FastAPI + [Uvicorn|Hypercorn|Daphne]
- FastAPI + [Uvicorn|Hypercorn|Daphne] + Gunicorn(Mutli-Threading)
- FastAPI + [Uvicorn|Hypercorn|Daphne] + Gunicorn(Mutli-Threading) + Nginx(Reverse Proxy)
- FastAPI + [Uvicorn|Hypercorn|Daphne] + Gunicorn(Mutli-Threading) + Nginx(Reverse Proxy) + CDN(Clouded Cache)
- FastAPI + [Uvicorn|Hypercorn|Daphne] + Gunicorn(Mutli-Threading) + Nginx(Reverse Proxy) + CDN(Clouded Cache) + OpenVPN(Security)


### CODE
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
$ PYTHONPATH=/home/[user]/anaconda3/lib/python3.12/site-packages gunicorn -k uvicorn.workers.UvicornWorker script:app
$ PYTHONPATH=/home/[user]/anaconda3/lib/python3.12/site-packages gunicorn -k uvicorn.workers.UvicornWorker script:app -b 0.0.0.0:8000
$ PYTHONPATH=/home/[user]/anaconda3/lib/python3.12/site-packages gunicorn -k uvicorn.workers.UvicornWorker script:app -b 0.0.0.0:8000 -w 4
$ PYTHONPATH=/home/[user]/anaconda3/lib/python3.12/site-packages gunicorn -k uvicorn.workers.UvicornWorker script:app --bind 0.0.0.0:8000 --workers 4
$ PYTHONPATH=/home/[user]/anaconda3/lib/python3.12/site-packages gunicorn -k uvicorn.workers.UvicornWorker script:app --bind 0.0.0.0:8000 --workers 4 --access-logfile -
```

---

```bash
$ which python
$ which pip
$ which uvicorn
$ which gunicorn
```


