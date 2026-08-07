from ex0 import CreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy, BattleStrategy


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            first_factory, first_strategy = opponents[i]
            second_factory, second_starategy = opponents[j]
            first_creature = first_factory.create_base()
            second_creature = second_factory.create_base()

            print("* Battle *")
            print(first_creature.describe())
            print(" vs.")
            print(second_creature.describe())
            print(" now fight!")
