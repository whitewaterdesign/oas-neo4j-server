from pydantic_settings import SettingsConfigDict,BaseSettings


class Config(BaseSettings):
    neo4j_uri: str = "neo4j://localhost:7687"
    neo4j_username: str
    neo4j_password: str
    mcp_host: str = "127.0.0.1"
    mcp_port: str = "8000"
    debug_mode: bool = False
    db_name: str = "neo4j"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

# @lru_cache()
def get_config():
    return Config()