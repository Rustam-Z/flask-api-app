import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///test.db")
todo = pd.read_sql("SELECT * FROM todo", engine)

data = pd.DataFrame(todo)
print(data)
