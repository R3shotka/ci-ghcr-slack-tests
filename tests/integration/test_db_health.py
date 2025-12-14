import os
import pytest
from app.db import ping_db

@pytest.mark.integration
def test_ping_db_postgres():
    # DATABASE_URL дає workflow (Postgres service)
    assert ping_db(os.environ["DATABASE_URL"]) is True
