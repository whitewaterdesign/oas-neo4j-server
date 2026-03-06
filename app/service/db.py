import datetime
from datetime import date

from neo4j import GraphDatabase

from app.core.config import get_config

config = get_config()
print(config)

driver = GraphDatabase.driver(config.neo4j_uri, auth=(config.neo4j_user, config.neo4j_password))
PRIMITIVES = (str, int, float, bool, type(None), date, datetime, datetime.time)
