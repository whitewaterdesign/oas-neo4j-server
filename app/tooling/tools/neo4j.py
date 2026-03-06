from typing import LiteralString, Dict

from neo4j import GraphDatabase, RoutingControl, Query

from app.tooling import mcp
from app.tooling.config import get_config


config = get_config()

driver = GraphDatabase.driver(
    config.neo4j_uri,
    auth=(config.neo4j_username, config.neo4j_password)
)


@mcp.tool()
def get_schema():
    """
    Returns the database schema (labels, relationship types, properties, constraints/indexes, and optionally sample counts).

    :return: Schema visualization records
    """
    query: LiteralString = r"CALL db.schema.visualization();"

    return run_cypher_query(query)


@mcp.tool()
def run_cypher_query(query: LiteralString | Query, parameters: Dict[str, str | int | bool] | None = None):
    """
    Executes a Cypher query and returns rows and metadata (and errors if any).

    :param query: LiteralString | Query - Cypher query string or Query object
    :param parameters: Dict[str, str] - Additional parameters for the query
    :return: Any - Query results
    """
    kwargs = parameters or {}

    records, _, _ = driver.execute_query(
        query,
        database_=config.db_name,
        routing_= RoutingControl.READ,
        **kwargs
    )

    return records
