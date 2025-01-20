from pydantic_settings import BaseSettings
# from pydantic import BaseSettings


from dotenv import load_dotenv
load_dotenv()  # Cargar variables desde .env antes de instanciar Settings



class Settings(BaseSettings):
    DATABASE_URL: str
    # SECRET_KEY: str
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()

