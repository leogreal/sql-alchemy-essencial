from pathlib import Path
from typing import Optional

import sqlalchemy as sa
from sqlalchemy.future.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from models.model_base import ModelBase

__engine: Optional[Engine] = None


def create_engine() -> Engine:
    global __engine

    if __engine:
        return

    file_db = "db/db.sqlite"
    folder = Path(file_db).parent
    folder.mkdir(parents=True, exist_ok=True)
    conn_str = f"sqlite:///{file_db}"
    __engine = sa.create_engine(
        url=conn_str,
        echo=False,
        connect_args={"check_same_thread": False},
    )

    return __engine


def create_session() -> Session:
    global __engine

    if not __engine:
        create_engine()

    session = sessionmaker(__engine, expire_on_commit=False, class_=Session)
    return session()


def create_tables() -> None:
    global __engine

    if not __engine:
        create_engine()

    import models.__all_models

    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)
