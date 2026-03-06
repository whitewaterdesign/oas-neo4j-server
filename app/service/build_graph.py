from app.model.info import InfoPartial
from typing import List
from neo4j import Driver
from app.model.spec import SpecPartial
from app.service.components import create_components_nodes
from app.service.external_docs import create_external_docs_nodes
from app.service.info import create_info_nodes
from app.service.paths import create_paths_nodes
from app.service.security import create_security_nodes
from app.service.server import create_server_nodes
from app.service.tag import create_tag_nodes


def create_graph(driver: Driver, open_api_spec: dict):
    spec = SpecPartial(**open_api_spec)
    errors: List[Exception] = []
    info = InfoPartial(**open_api_spec.get('info') or {})
    title = info.title if info.title else 'oas-spec'

    output = (title, errors)

    with driver.session() as session:
        # Central node
        session.run("MERGE (a:Api { title: $title })", title=title)

        # Openapi spec version
        if open_api_spec.get('openapi'):
            session.run("MERGE (a:Api { title: $title }) SET a.openapi = $openapi", title=title,
                        openapi=open_api_spec.get('openapi'))

        # Info
        create_info_nodes(session, title, info)

        # Servers
        create_server_nodes(session, title, spec.servers)

        # Tags
        create_tag_nodes(session, title, spec.tags)

        # Security
        create_security_nodes(session, title, spec.security)

        # Paths
        create_paths_nodes(session, title, spec.paths)

        # External Docs
        create_external_docs_nodes(session, title, spec.externalDocs)

        # Components
        create_components_nodes(session, title, spec.components)

        session.close()

        return output
