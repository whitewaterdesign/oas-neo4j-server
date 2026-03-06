from typing import List

from neo4j import Session

from app.model.tag import TagPartial


def create_tag_nodes(session: Session, title: str, tags: List[TagPartial]):
    for tag in tags:
        name = tag.name or tag.description
        tag_dict = {
            "title": title,
            "name": name
        }
        session.run("MERGE (a:Api { name: $title }) MERGE (a)-[:HAS_TAG]->(t: Tag { name: $title, name: $name })", **tag_dict)
        session.run("""
            MATCH (t: Tag { name: $title, name: $name })
            SET t.description = $description
        """, description=tag.description, **tag_dict)

        if tag.externalDocs:
            print(tag.externalDocs)
            session.run("""
                MATCH (t:Tag {name: $title, name: $name}) MERGE (t)-[:HAS_EXTERNAL_DOCS]->(ed:ExternalDocs { description: $description, url: $url })            
            """, **dict(tag.externalDocs), **tag_dict)
