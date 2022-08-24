from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str = None


class SignUp(BaseModel):
    username: str
    password: str
    email: str
    code: str


class PasswordReset(BaseModel):
    password1: str
    email: str
    code: str


class UpdateAvatar(BaseModel):
    u_id: int
    name: str
    imgB64: str
    flag: str
