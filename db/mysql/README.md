`create_engine`
```python
import pandas as pd
from sqlalchemy import create_engine, text

user = "root"
password = "PASSWORD"
host = "localhost"
port = 3306
dbname = "mysql"

try:
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}")
    with engine.connect() as conn:
        result = conn.execute(text("""SHOW DATABASES"""))
        pd.DataFrame(result.fetchall())
        print("Connection Success")
except Exception as e:
    print(f"Connection Fail: {e}")
```

`create_async_engine`
```python
import pandas as pd
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

user = "root"
password = "PASSWORD"
host = "localhost"
port = 3306
dbname = "mysql"

try:
    engine = create_async_engine(
        f"mysql+asyncmy://{user}:{password}@{host}:{port}/{dbname}",
        echo=False,
    )
    async with engine.connect() as conn:  # type: AsyncConnection
        result = await conn.execute(text("""SHOW DATABASES"""))
        df = pd.DataFrame(result.fetchall())
        print("Connection Success")
except Exception as e:
    print(f"Connection Fail: {e}")

```
