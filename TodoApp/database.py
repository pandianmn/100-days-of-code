from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URI = "sqlite:///./todos.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
)
