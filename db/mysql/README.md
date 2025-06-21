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
        pd.DataFrame(
            conn.execute(
                text("""
                    show databases
                """)
            ).fetchall()
        )
        print("Connection Success")
except Exception as e:
    print(f"Connection Fail: {e}")
```
