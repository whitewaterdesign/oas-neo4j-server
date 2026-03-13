from neo4j import Session

from app.model.paths import PathItemPartial, OperationPartial, ParameterPartial, Parameter, Reference

def create_reference_node(session: Session, title: str, path: str, reference: Reference):
    pass

def create_parameters_node(session: Session, title: str, path:str, method:str, parameter: Parameter | Reference):
    pass
    # params = parameter.model_dump()
    # props = {
    #     "name": params.get('name'),
    #     "in": params.get('in_param'),
    #     "description": params.get('description'),
    #     "required": params.get('required'),
    #     "deprecated": params.get('deprecated'),
    #     "allowEmptyValue": params.get('allowEmptyValue'),
    #     "style": params.get('style'),
    #     "explode": params.get('explode'),
    #     "allowReserved": params.get('allowReserved'),
    # }
    # if parameter.param_schema:
    #     props['param_schema'] = parameter.param_schema
    #
    # session.run("""
    #     MATCH (a:Api {name: $title})-[:HAS_PATH]->(p:Path {name: $path})-[:HAS_METHOD]->(m:Method {method: $method})
    #     MERGE (m)-[:HAS_PARAMETER]->(p:Parameter {name: $props.name})
    #     SET p += $props
    # """, title=title, path=path, method=method, props=props)

def create_paths_nodes(session: Session, title: str, paths: dict[str, PathItemPartial]):
    for path, path_item in paths.items():
        session.run("""
            MATCH (a:Api { name: $title })
            MERGE (a)-[:HAS_PATH]->(p:Path { name: $path });
        """, title=title, path=path)
        for name, field in path_item.model_fields.items():
            value = getattr(path_item, name)
            if isinstance(value, OperationPartial):
                print(value)
                props = {
                    "operationId": value.operationId,
                    "summary": value.summary,
                    "description": value.description,
                    "deprecated": value.deprecated,
                    "tags": value.tags or [],
                    "name": name,
                }
                session.run("""
                    MATCH (a:Api {name: $title})-[:HAS_PATH]->(p:Path {name: $path})
                    MERGE (p)-[:HAS_METHOD]->(m: Method { method: $method })
                    SET m += $props
                """, title=title, path=path, method=name, props=props)
                if value.externalDocs:
                    pass
                if value.parameters:
                    for parameter in value.parameters:
                        if isinstance(parameter, ParameterPartial) or isinstance(parameter, Parameter):
                            create_parameters_node(session, title, path, name, parameter)

        # print(path, path_item.model_dump())
        # session.run("MATCH (a:Api { name: $title }) MERGE (a)-[:HAS_PATH]->(p:Path { name: $title });", title=title)

