from datetime import datetime

import sqlalchemy as sa

from models.model_base import ModelBase


class FoodPreservative(ModelBase):
    __tablename__: str = "food_preservatives"

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    created_at: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    name: str = sa.Column(sa.String(45), unique=True, nullable=False)
    description: str = sa.Column(sa.String(150), nullable=False)

    def __repr__(self) -> str:
        return f"<FoodPreservative: {self.name}>"
