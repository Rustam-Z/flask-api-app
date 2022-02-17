import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///test.db")
todos = pd.read_sql("SELECT * FROM todo", engine)
data = pd.DataFrame(todos)

if __name__ == "__main__":
    print(data)
