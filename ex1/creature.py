from ex0.creature import Creature, CreatureFactory
from .capability import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self.is_transform = False

    def attack(self) -> str:
        if self.is_transform:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."

    def transform(self) -> str:
        self.is_transform = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transform = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        self.is_transform = False

    def attack(self) -> str:
        if self.is_transform:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."

    def transform(self) -> str:
        self.is_transform = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_transform = False
        return "Morphagon stabilizes its form."


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
