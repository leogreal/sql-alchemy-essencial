from datetime import datetime

import sqlalchemy as sa

from models.model_base import ModelBase


class Reseller(ModelBase):
    __tablename__: str = "resellers"

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    created_at: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    name: str = sa.Column(sa.String(45), unique=True, nullable=False)
    company_name: str = sa.Column(sa.String(100), nullable=False)
    contact: str = sa.Column(sa.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"<Reseller: {self.name}>"