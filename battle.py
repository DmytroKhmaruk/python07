from ex0 import CreatureFactory, AquaFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())

    print(evolved.describe())
    print(evolved.attack())


def test_battle(f_factory: CreatureFactory,
                s_factory: CreatureFactory) -> None:
    f_creature = f_factory.create_base()
    s_creature = s_factory.create_base()

    print(f_creature.describe())
    print(" vs.")
    print(s_creature.describe())
    print(" fight!")
    print(f_creature.attack())
    print(s_creature.attack())


if __name__ == "__main__":
    aqua_factory = AquaFactory()
    flame_factory = FlameFactory()

    print("Testing factory")
    test_factory(flame_factory)

    print("\nTesting factory")
    test_factory(aqua_factory)

    print("\nTesting battle")
    test_battle(flame_factory, aqua_factory)
