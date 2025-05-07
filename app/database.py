from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from contextlib import contextmanager
import os

DATABASE_URL = os.getenv("DATABASE_URL")
# Prod database URL
HEROKU_POSTGRESQL_NAVY_URL = os.getenv("HEROKU_POSTGRESQL_NAVY_URL")
if DATABASE_URL is None:
    DATABASE_URL = HEROKU_POSTGRESQL_NAVY_URL.replace("postgres://", "postgresql://")

engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)


def create_tables():
    """Create tables in the database."""
    Base.metadata.create_all(bind=engine)


@contextmanager
def get_session():
    """Provide a transactional scope around a series of operations."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()