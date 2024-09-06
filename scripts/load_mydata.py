import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# Create a PostgreSQL engine
engine = create_engine('postgresql://postgres:pgadmin@localhost:5432/tellco')

# Define a function to load data from PostgreSQL
def load_data(table_name):
    try:
        # Construct and execute the query
        query = f"SELECT * FROM {table_name};"
        df = pd.read_sql(query, engine)
        return df
    except SQLAlchemyError as e:
        print(f"An error occurred while loading data: {e}")
        return None
    finally:
        # Optional: Explicitly dispose of the engine (close connections)
        engine.dispose()
