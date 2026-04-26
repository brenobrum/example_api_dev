from pydantic_settings import BaseSettings

class Env(BaseSettings):
    pass

env: Env = Env()