from conf.db_session import create_session
from models.flavor import Flavor
from models.food_preservative import FoodPreservative
from models.ingredient import Ingredient
from models.nutritional_additive import NutritionalAdditive
from models.packaging_type import PackagingType
from models.popsicle_type import PopsicleType


def insert_nutritional_additive() -> None:
    print("Registering nutritional additive")

    name: str = input("Enter the name of the nutritional additive: ")
    chemical_formula: str = input(
        "Enter the chemical formula of the nutritional additive: "
    )
    nutritional_additive: NutritionalAdditive = NutritionalAdditive(
        name=name, chemical_formula=chemical_formula
    )

    with create_session() as session:
        session.add(nutritional_additive)
        session.commit()

    print("Nutritional additive was successfully registered!")
    print(f"Id: {nutritional_additive.id}")
    print(f"Created at: {nutritional_additive.created_at}")
    print(f"Name: {nutritional_additive.name}")
    print(f"Chemical formula: {nutritional_additive.chemical_formula}")


def insert_flavor() -> None:
    print("Registering flavor")

    name: str = input("Enter the name of the flavor: ")
    flavor: Flavor = Flavor(name=name)

    with create_session() as session:
        session.add(flavor)
        session.commit()

    print("Flavor was successfully registered!")
    print(f"Id: {flavor.id}")
    print(f"Created at: {flavor.created_at}")
    print(f"Name: {flavor.name}")


def insert_packaging_type() -> None:
    print("Registering packaging type")

    name: str = input("Enter the name of the packaging type: ")
    packaging_type: PackagingType = PackagingType(name=name)

    with create_session() as session:
        session.add(packaging_type)
        session.commit()

    print("Packaging type was successfully registered!")
    print(f"Id: {packaging_type.id}")
    print(f"Created at: {packaging_type.created_at}")
    print(f"Name: {packaging_type.name}")


def insert_popsicle_type() -> None:
    print("Registering popsicle_type")

    name: str = input("Enter the name of the popsicle type: ")
    popsicle_type: PopsicleType = PopsicleType(name=name)

    with create_session() as session:
        session.add(popsicle_type)
        session.commit()

    print("Popsicle type was successfully registered!")
    print(f"Id: {popsicle_type.id}")
    print(f"Created at: {popsicle_type.created_at}")
    print(f"Name: {popsicle_type.name}")


def insert_ingredient() -> None:
    print("Registering ingredient")

    name: str = input("Enter the name of the ingredient: ")
    ingredient: Ingredient = Ingredient(name=name)

    with create_session() as session:
        session.add(ingredient)
        session.commit()

    print("Ingredient was successfully registered!")
    print(f"Id: {ingredient.id}")
    print(f"Created at: {ingredient.created_at}")
    print(f"Name: {ingredient.name}")


def insert_food_preservative() -> None:
    print("Registering food preservative")

    name: str = input("Enter the name of the food preservative: ")
    description: str = input("Enter the description of the food preservative: ")
    food_preservative: FoodPreservative = FoodPreservative(
        name=name, description=description
    )

    with create_session() as session:
        session.add(food_preservative)
        session.commit()

    print("Food preservative was successfully registered!")
    print(f"Id: {food_preservative.id}")
    print(f"Created at: {food_preservative.created_at}")
    print(f"Name: {food_preservative.name}")
    print(f"Description: {food_preservative.description}")


if __name__ == "__main__":
    # insert_nutritional_additive()
    # insert_flavor()
    # insert_packaging_type()
    # insert_popsicle_type()
    # insert_ingredient()
    insert_food_preservative()
