from pydantic import BaseModel


class Blogs(BaseModel):
    content: str
    images: list = []
    blog_id: str = ''
    parent_id: int = None


class UploadImg(BaseModel):
    user_id: int
    file: str