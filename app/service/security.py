from typing import List

from neo4j import Session

from app.model.security import SecurityPartial


def create_security_nodes(session: Session, title: str, security: List[SecurityPartial]):
    pass
