from pydantic_settings import SettingsConfigDict,BaseSettings


class Config(BaseSettings):
    mcp_host: str = "localhost"
    mcp_port: str = "8000"
    mcp_url: str = "http://localhost:8000"
    openai_api_key: str

    neo4j_uri: str = "bolt://localhost:7687"
    neo4j_user: str = "neo4j"
    neo4j_password: str = "password"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

# @lru_cache()
def get_config():
    return Config()
