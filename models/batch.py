from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, relationship

from models.model_base import ModelBase
from models.popsicle_type import PopsicleType


class Batch(ModelBase):
    __tablename__: str = "batches"

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    created_at: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    popsicle_id: int = sa.Column(sa.Integer, sa.ForeignKey("popsicle_types.id"))
    popsicle_type: Mapped[PopsicleType] = relationship("PopsicleType", lazy="joined")
    quantity: int = sa.Column(sa.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"<Batch: {self.id} {self.quantity}>"
