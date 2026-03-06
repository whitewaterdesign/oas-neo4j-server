from neo4j import Session

from app.model.info import InfoPartial
from app.service.db import PRIMITIVES


def create_info_nodes(session: Session, title: str, info: InfoPartial):
    info_primitives = {key: value for key, value in dict(info).items() if type(value) in PRIMITIVES}

    session.run("MATCH (a:Api { name: $title }) MERGE (a)-[:HAS_INFO]->(i:Info { name: $title });", title=title)
    session.run("MERGE (i: Info { name: $title }) SET i += $info;", title=title, info=info_primitives)

    if info.contact:
        session.run("MATCH (a:Api { name: $title }) MERGE (a)-[:HAS_CONTACT]->(co: Contact { name: $title })",
                    title=title)
        session.run("MERGE (co: Contact { name: $title }) SET co += $contact;", title=title,
                    contact=dict(info.contact))

    if info.license:
        session.run("MATCH (a:Api { name: $title }) MERGE (a)-[:HAS_LICENSE]->(l: License { name: $title })",
                    title=title)
        session.run("MERGE (l: License { name: $title }) SET l += $license;", title=title, license=dict(info.license))
