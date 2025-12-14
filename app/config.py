from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_hostname : str = ""
    database_port : int  = 0000
    database_password : str = ""
    database_name : str = ""
    database_username : str = ""
    secret_key : str = ""
    algorithm : str = ""
    access_token_expire_minute : int = 8000

    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8",
        extra = "ignore"
    )


settings = Settings()