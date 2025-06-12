## python-requests

```python
import requests

requests.get("http://localhost:8000").json()
requests.get("http://localhost:8000", params={"Key": "Name"}).json() # Query String
requests.post("http://localhost:8000", data={"Key01": "Value01", "Key02": "Value02"}).json()
requests.put("http://localhost:8000", json={"Key01": "Value01", "Key02": "Value02"}).json()
requests.patch("http://localhost:8000", json={"Key01": "Value01", "Key02": "Value02"}).json()
requests.delete("http://localhost:8000").json()
```
