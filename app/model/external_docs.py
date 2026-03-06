from pydantic import BaseModel


class ExternalDocs(BaseModel):
    description: str | None = None
    url: str

class ExternalDocsPartial(BaseModel):
    description: str | None = None
    url: str | None = None
