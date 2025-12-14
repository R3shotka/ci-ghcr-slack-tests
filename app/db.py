import os
from sqlalchemy import create_engine, text

def database_url() -> str:
    return os.getenv("DATABASE_URL", "sqlite+pysqlite:///:memory:")

def ping_db(url: str | None = None) -> bool:
    engine = create_engine(url or database_url(), pool_pre_ping=True)
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return True
