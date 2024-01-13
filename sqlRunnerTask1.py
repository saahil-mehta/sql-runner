# %%
import os
from google.cloud.sql.connector import Connector
import sqlalchemy
import configs

# %%
# Loading configurations
configurations = configs.configurations

# Set Google Application Credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = configurations["GOOGLE_APPLICATION_CREDENTIALS_PATH"]

# %%
def getconn() -> sqlalchemy.engine.base.Connection:
    with Connector() as connector:
        return connector.connect(
            configurations["GCP_SQL_CONNECTION_NAME"],
            configurations["DATABASE_DRIVER"],
            user=configurations["DATABASE_USER"],
            password=configurations["DATABASE_PASSWORD"],
            db=configurations["DATABASE_NAME"]
        )

# %%
# Create SQLAlchemy Engine
def init_connection_engine():
    engine = sqlalchemy.create_engine(
        configurations["DATABASE_URL"],
        creator=getconn,
    )
    return engine

# %%
# Function to Execute Queries
def execute_query(query):
    engine = init_connection_engine()
    with engine.connect() as connection:
        result = connection.execute(query)
        for row in result:
            print(row)
    engine.dispose()


