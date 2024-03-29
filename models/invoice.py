from datetime import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

from models.batch import Batch
from models.model_base import ModelBase
from models.reseller import Reseller

invoices_batches = sa.Table(
    "invoices_batches",
    ModelBase.metadata,
    sa.Column("invoice_id", sa.Integer, sa.ForeignKey("invoices.id")),
    sa.Column("batch_id", sa.Integer, sa.ForeignKey("batches.id")),
)


class Invoice(ModelBase):
    __tablename__: str = "invoices"

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    created_at: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    purchase_value: float = sa.Column(sa.DECIMAL(8, 2), nullable=False)
    serial_number: str = sa.Column(sa.String(45), unique=True, nullable=False)
    description: str = sa.Column(sa.String(200), nullable=False)
    reseller_id: int = sa.Column(sa.Integer, sa.ForeignKey("resellers.id"))
    reseller: Reseller = orm.relationship("Reseller", lazy="joined")

    batches: list[Batch] = orm.relationship(
        "Batch", secondary=invoices_batches, backref="batch", lazy="dynamic"
    )

    def __repr__(self) -> str:
        return f"<Invoice: {self.serial_number}>"
