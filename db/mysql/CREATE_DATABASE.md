```python
import pandas as pd
from sqlalchemy import create_engine, text

user = "root"
password = "PASSWORD"
host = "localhost"
port = 3306

try:
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}")
    with engine.connect() as conn:
        dbname = "mysql"
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {dbname}"))
        subengine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}")
        with subengine.connect() as conn:    
            result = conn.execute(text("""SHOW DATABASES"""))
            df = pd.DataFrame(result.fetchall())
            display(df)
        print("Connection Success")
except Exception as e:
    print(f"Connection Fail: {e}")
```
