from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Note: for async sqlite we use aiosqlite, but to keep dependencies simple and since we might switch to postgres,
# we'll use standard sync sqlite via SQLAlchemy for the MVP, or just require aiosqlite.
# Actually, since FastAPI is async, aiosqlite is better. Let's assume standard sync for now to avoid extra pip installs.
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine(
    settings.DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
