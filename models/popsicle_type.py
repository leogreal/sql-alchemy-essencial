from datetime import datetime

import sqlalchemy as sa

from models.model_base import ModelBase


class PopsicleType(ModelBase):
    __tablename__: str = "popsicle_types"

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_at: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    name: str = sa.Column(sa.String(45), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"<PopsicleType: {self.name}>"
