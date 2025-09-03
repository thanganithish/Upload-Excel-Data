from pydantic import BaseModel

class UploadRequest(BaseModel):
    description: str | None = None
