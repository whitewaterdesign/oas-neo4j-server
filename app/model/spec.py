from typing import Optional, List

from pydantic import BaseModel, ConfigDict

from app.model.components import Components, ComponentsPartial
from app.model.external_docs import ExternalDocsPartial, ExternalDocs
from app.model.info import InfoPartial, Info
from app.model.paths import PathItemPartial, PathItem
from app.model.security import Security, SecurityPartial
from app.model.server import ServerPartial, Server
from app.model.tag import TagPartial, Tag


class SpecPartial(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    openapi: Optional[str] = None
    info: InfoPartial
    servers: Optional[List[ServerPartial]] = None
    paths: Optional[dict[str, PathItemPartial]] = None
    components: Optional[ComponentsPartial] = None
    security: Optional[List[SecurityPartial]] = None
    tags: Optional[List[TagPartial]] = None
    externalDocs: Optional[ExternalDocsPartial] = None

class Spec(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    openapi: str
    info: Info
    servers: Optional[List[Server]] = None
    paths: dict[str, PathItem]
    components: Optional[Components] = None
    security: Optional[List[Security]] = None
    tags: Optional[List[Tag]] = None
    externalDocs: Optional[ExternalDocs] = None
