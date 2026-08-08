from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy, AggressiveStrategy, DefensiveStrategy, BattleStrategy,
    InvalidStrategyError)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            first_factory, first_strategy = opponents[i]
            second_factory, second_starategy = opponents[j]
            first_creature = first_factory.create_base()
            second_creature = second_factory.create_base()

            print("\n* Battle *")
            print(first_creature.describe())
            print(" vs.")
            print(second_creature.describe())
            print(" now fight!")

            try:
                first_strategy.act(first_creature)
                second_starategy.act(second_creature)
            except InvalidStrategyError as e:
                print(e)
                return


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    tournament_0 = [
        (flame_factory, normal),
        (healing_factory, defensive)]
    battle(tournament_0)

    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    tournament_1 = [
        (flame_factory, aggressive),
        (healing_factory, defensive)]
    battle(tournament_1)

    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    tournament_2 = [
        (aqua_factory, normal),
        (healing_factory, defensive),
        (transform_factory, aggressive)]
    battle(tournament_2)
