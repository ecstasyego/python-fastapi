## bash-curl
```bash
$ curl 127.0.0.1:8000 # [body]
$ curl -i 127.0.0.1:8000 # --include # [header&body]
$ curl -I 127.0.0.1:8000 # --head # [header]
$ curl -s 127.0.0.1:8000 # --silent # [body]
$ curl -L 127.0.0.1:8000 # --location # [redirection]
```

```bash
$ curl 127.0.0.1:8000 # [GET|BODY]
$ curl -I 127.0.0.1:8000 # [GET|HEADER]
$ curl -X GET 127.0.0.1:8000 # [GET|BODY]
$ curl -X GET 127.0.0.1:8000?Key=Value # [GET]: Read
$ curl -X POST -d "Key=Value" 127.0.0.1:8000 # [POST]: Create, Append
$ curl -X PUT -d '{"Key":"Value"}' 127.0.0.1:8000 # [PUT]: Update All
$ curl -X PATCH -d '{"Key":"Value"}' 127.0.0.1:8000 # [PATCH]: Update Partial
$ curl -X DELETE 127.0.0.1:8000 # [DELETE]: Delete
$ curl -X OPTIONS 127.0.0.1:8000 # [OPTIONS]
```

```bash
# Query String
$ curl [URL(Uniform Resource Locator)]
$ curl [Scheme://User@Host:Port/Path?Query#Fragment]
$ curl [Scheme://User@Host:Port/Path?Key1=Value1#Fragment]
$ curl [Scheme://User@Host:Port/Path?Key1=Value1&Key2=Value2#Fragment]
$ curl -G -d "Key1=Value1" -d "Key2=Value2" [Scheme://User@Host:Port/Path#Fragment]
$ curl -X POST -d "Key1=Value1&Key2=Value2" [Scheme://User@Host:Port/Path#Fragment]
```


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
