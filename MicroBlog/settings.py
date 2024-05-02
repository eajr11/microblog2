from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DBNAME: str = "postgres"
    DBUSER: str = "postgres"
    DBPASSWORD: str = "postgres"
    DBHOST: str = "localhost"
    DBPORT: str = "5432"

    @property
    def PG_DSN(self):
        return f"postgresql://{self.DBUSER}:{self.DBPASSWORD}@{self.DBHOST}:{self.DBPORT}/{self.DBNAME}"

    class Config:
        env_file = ".env"


config = Settings()
