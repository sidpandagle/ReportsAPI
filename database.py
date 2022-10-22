from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./report.db"
SQLALCHEMY_DATABASE_URL = "postgresql://keiobbkm:Orknb-PfiycWTkC6RX5Vl_cebgDFgOS3@satao.db.elephantsql.com/keiobbkm"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(bind=engine,autocommit=False, autoflush=False)
 
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


