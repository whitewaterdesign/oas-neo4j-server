from typing import List, Any

from pydantic import BaseModel, ConfigDict, Field

from app.model.external_docs import ExternalDocsPartial, ExternalDocs
from app.model.server import Server, ServerPartial

class Reference(BaseModel):
    ref: str | None = Field(default=None, alias="$ref")

class Example(BaseModel):
    summary: str | None = None
    description: str | None = None
    value: Any | None = None
    externalValue: str | None = None

class Header(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    description: str | None = None
    required: bool | None = None
    deprecated: bool | None = None
    allowEmptyValue: bool | None = None
    style: str | None = None
    explode: bool | None = None
    allowReserved: bool | None = None
    header_schema: dict | None = Field(default=None, alias="schema")
    example: Any | None = None

class Encoding(BaseModel):
    contentType: str | None = None
    headers: dict[str, Header | Reference] | None = None
    style: str | None = None
    explode: bool | None = None
    allowReserved: bool | None = None

class Media(BaseModel):
    media_schema: dict | Reference | None = Field(default=None, alias="schema")
    example: Any | None = None
    examples: dict[str, Reference | Example] | None = None
    encoding: dict[str, Encoding] | None = None
    
class Links(BaseModel):
    operationRef: str | None = None
    operationId: str | None = None
    parameters: dict[str, Any] | None = None
    requestBody: Any | None = None
    description: str | None = None
    server: ServerPartial | None = None

class Response(BaseModel):
    description: str | None = None
    headers: dict[str, Header | Reference] | None = None
    content: dict[str, Media] | None = None
    links: dict[str, Links | Reference] | None = None

class Parameter(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str
    in_param: str = Field(default=None, alias="in")
    description: str | None = None
    required: bool | None = None
    deprecated: bool | None = None
    allowEmptyValue: bool | None = None
    style: str | None = None
    explode: bool | None = None
    allowReserved: bool | None = None
    param_schema: dict | None = Field(default=None, alias="schema")
    example: Any | None = None

    def model_dump(self, **kwargs):
        data = super().model_dump(by_alias=True, exclude_none=True, **kwargs)

        # Custom transformation example:
        if self.in_param:
            data["in"] = self.in_param

        return data

class ParameterPartial(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str | None = None
    in_param: str | None = Field(default=None, alias="in")
    description: str | None = None
    required: bool | None = None
    deprecated: bool | None = None
    allowEmptyValue: bool | None = None
    style: str | None = None
    explode: bool | None = None
    allowReserved: bool | None = None
    param_schema: dict | None = Field(default=None, alias="schema")
    example: Any | None = None

class RequestBody(BaseModel):
    description: str
    content: dict[str, Media]
    required: bool = False

class Operation(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    responses: dict[str, Response | Reference] | None = None
    tags: List[str] | None = None
    summary: str | None = None
    description: str | None = None
    externalDocs: ExternalDocs | None = None
    operationId: str | None = None
    parameters: List[Parameter | Reference] | None = None
    requestBody: Reference | RequestBody | None = None
    deprecated: bool | None = None
    security: List[dict] | None = None
    servers: List[Server] | None = None

class OperationPartial(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    tags: List[str] | None = None
    summary: str | None = None
    description: str | None = None
    operationId: str | None = None
    deprecated: bool | None = None

    responses: Response | None = None
    externalDocs: ExternalDocsPartial | None = None
    parameters: List[Parameter | Reference] | None = None
    requestBody: Reference | RequestBody | None = None
    security: List[dict] | None = None
    servers: List[ServerPartial] | None = None
    callbacks: dict[str, Reference | dict[str, 'PathItem']] | None = None

class PathItemPartial(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    ref: str | None = Field(default=None, alias="$ref")
    summary: str | None = None
    description: str | None = None
    get: OperationPartial | None = None
    put: OperationPartial | None = None
    post: OperationPartial | None = None
    delete: OperationPartial | None = None
    options: OperationPartial | None = None
    head: OperationPartial | None = None
    patch: OperationPartial | None = None
    trace: OperationPartial | None = None
    servers: List[ServerPartial] | None = None
    parameters: List[ParameterPartial | Reference] | None = None

class PathItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    ref: str | None = Field(default=None, alias="$ref")
    summary: str | None = None
    description: str | None = None
    get: Operation | None = None
    put: Operation | None = None
    post: Operation | None = None
    delete: Operation | None = None
    options: Operation | None = None
    head: Operation | None = None
    patch: Operation | None = None
    trace: Operation | None = None
    servers: List[Server] | None = None
    parameters: List[Parameter | Reference] | None = None



