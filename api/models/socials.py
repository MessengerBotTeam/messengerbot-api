from pydantic import BaseModel


class Social(BaseModel):
    name: str
    url: str
    highlight: bool  # high priority than other social


class SocialsResponse(BaseModel):
    socials: list[Social]
