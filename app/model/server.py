from typing import Optional

from pydantic import BaseModel


class Server(BaseModel):
    url: str
    description: Optional[str] = None
    variables: Optional[dict] = None

class ServerPartial(BaseModel):
    url: Optional[str] = None
    description: Optional[str] = None
    variables: Optional[dict] = None
