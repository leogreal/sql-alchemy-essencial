from datetime import datetime
from typing import Optional

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, relationship

from models.flavor import Flavor
from models.food_preservative import FoodPreservative
from models.ingredient import Ingredient
from models.model_base import ModelBase
from models.nutritional_additive import NutritionalAdditive
from models.packaging_type import PackagingType
from models.popsicle_type import PopsicleType

popsicles_ingredients = sa.Table(
    "popsicles_ingredients",
    ModelBase.metadata,
    sa.Column("popsicle_id", sa.Integer, sa.ForeignKey("popsicles.id")),
    sa.Column("ingredient_id", sa.Integer, sa.ForeignKey("ingredients.id")),
)

popsicles_food_preservatives = sa.Table(
    "popsicles_food_preservatives",
    ModelBase.metadata,
    sa.Column("popsicle_id", sa.Integer, sa.ForeignKey("popsicles.id")),
    sa.Column(
        "food_preservative_id", sa.Integer, sa.ForeignKey("food_preservatives.id")
    ),
)

popsicles_nutritional_additives = sa.Table(
    "popsicles_nutritional_additives",
    ModelBase.metadata,
    sa.Column("popsicle_id", sa.Integer, sa.ForeignKey("popsicles.id")),
    sa.Column(
        "nutritional_additive_id", sa.Integer, sa.ForeignKey("nutritional_additives.id")
    ),
)


class Popsicle(ModelBase):
    __tablename__: str = "popsicles"

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_at: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    price: float = sa.Column(sa.DECIMAL(8, 2), nullable=False)
    flavor_id: int = sa.Column(sa.Integer, sa.ForeignKey("flavors.id"))
    flavor: Mapped[Flavor] = relationship("Flavor", lazy="joined")
    packaging_type_id: int = sa.Column(sa.Integer, sa.ForeignKey("packaging_types.id"))
    packaging_type: Mapped[PackagingType] = relationship("PackagingType", lazy="joined")
    popsicle_type_id: int = sa.Column(sa.Integer, sa.ForeignKey("popsicle_types.id"))
    popsicle_type: Mapped[PopsicleType] = relationship("PopsicleType", lazy="joined")

    ingredients: Mapped[list[Ingredient]] = relationship(
        "Ingredient",
        secondary=popsicles_ingredients,
        backref="ingredient",
        lazy="joined",
    )

    food_preservative: Mapped[Optional[list[FoodPreservative]]] = relationship(
        "FoodPreservative",
        secondary=popsicles_food_preservatives,
        backref="food_preservative",
        lazy="joined",
    )

    nutritional_additive: Mapped[Optional[list[NutritionalAdditive]]] = relationship(
        "NutritionalAdditive",
        secondary=popsicles_nutritional_additives,
        backref="nutritional_additive",
        lazy="joined",
    )

    def __repr__(self) -> str:
        return f"<Popsicle: {self.popsicle_type.name} with flavor {self.flavor.name} and price {self.price}>"
