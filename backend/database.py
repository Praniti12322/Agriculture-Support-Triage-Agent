from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./history.db"
engine = create_engine(DATABASE_URL, echo=False)


def get_session():
    with Session(engine) as session:
        yield session


def init_db():
    # create tables if they don't exist
    SQLModel.metadata.create_all(engine)
