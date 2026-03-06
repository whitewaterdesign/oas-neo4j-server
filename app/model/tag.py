from pydantic import BaseModel

from app.model.external_docs import ExternalDocsPartial


class Tag(BaseModel):
    name: str
    description: str | None = None
    externalDocs: ExternalDocsPartial | None = None

class TagPartial(BaseModel):
    name: str
    description: str | None = None
    externalDocs: ExternalDocsPartial | None = None
