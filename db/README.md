### Synchronous

```python
from fastapi import FastAPI

app = FastAPI()

def heavy_calculation(n):
    return n

@app.get("/")
def processing(n: int):
    result = heavy_calculation(n)
    return {"result": result}
```
```bash
$ uvicorn script:app --host 0.0.0.0 --port 8000 --reload
```

### Asynchronous
`script.py`
```python
from fastapi import FastAPI
from concurrent.futures import ThreadPoolExecutor

app = FastAPI()
executor = ThreadPoolExecutor(max_workers=5)

def heavy_calculation(n):
    return n

@app.get("/")
async def processing(n: int):
    result = await asyncio.get_running_loop().run_in_executor(executor, heavy_calculation, n)
    return {"result": result}
```
```bash
$ uvicorn script:app --host 0.0.0.0 --port 8000 --reload
```
