from pydantic import BaseModel


class Contact(BaseModel):
    name: str | None = None
    url: str | None = None
    email: str | None = None

class LicensePartial(BaseModel):
    name: str | None = None
    url: str | None = None

class License(BaseModel):
    name: str
    url: str | None = None

class InfoPartial(BaseModel):
    title: str | None = None
    description: str | None = None
    termsOfService: str | None = None
    contact: Contact | None = None
    license: LicensePartial | None = None
    version: str | None = None

class Info(BaseModel):
    title: str
    version: str
    description: str | None = None
    termsOfService: str | None = None
    contact: Contact | None = None
    license: License | None = None
