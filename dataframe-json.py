import pandas as pd
import numpy as np

from fastapi import FastAPI
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # note: distribution-limit
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/path/")
def read_table():
    conn = sqlite3.connect(":memory:")

    pd.DataFrame(np.random.randint(0, 3, size=(30, 3)), columns=list('ABC')).map(lambda x: dict(enumerate(['a', 'b', 'c']))[x]).to_sql('data_sample', conn, index=False)
    df = pd.read_sql('select * from data_sample', conn)

    conn.close()

    return [{"col0": row[df.columns[0]], "col1": row[df.columns[1]], "col2": row[df.columns[2]]} for idx, row in df.iterrows()]
