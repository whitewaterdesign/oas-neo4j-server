from typing import List

from neo4j import Session

from app.model.server import ServerPartial


def create_server_nodes(session: Session, title: str, servers: List[ServerPartial] | None = None):
    if servers is None:
        servers = []
    for server in servers:
        create_server_node(session, title, server)


def create_server_node(session: Session, title: str, server: ServerPartial):
    url = server.url
    description = server.description
    server_id = {
        "url": url,
        "title": title
    }

    session.run("MATCH (a:Api { name: $title }) MERGE (a)-[:HAS_SERVER]->(s: Server { url: $url, name: $title })",
                **server_id)

    if description:
        session.run("""
            MERGE (s:Server {url: $url, name: $title})
            SET s.description = $description
            """, description=description, **server_id)

    if server.variables:
        session.run("""
            MERGE (s:Server {url: $server.url, name: $title})
            SET s += $variables
            """, variables=server.variables, **server_id)
