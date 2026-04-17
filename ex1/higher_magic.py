from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def call_spell(target: str, power: int) -> tuple:
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return (res1, res2)

    return call_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def power_magic(target: str, power: int) -> int:
        res1 = base_spell(target, power * multiplier)
        return res1

    return power_magic


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str | Callable:
        if condition(target, power):
            return spell(target, power)
        return "spell fizzled"

    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_all(name: str, power: int) -> list:
        res_list = []
        for spell in spells:
            res_list.append(spell(name, power))
        return res_list

    return cast_all


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def power_spell(target: str, power: int) -> int:
    return power


def fire(target: str, power: int) -> str:
    return f"{target} has {power} fire"


def ice_moula(target: str, power: int) -> str:
    return f"{target} made a lot of {power}"


def damn_broski(target: str, power: int) -> str:
    return f"Damn the fendi suits you well {target}, you have {power} moula "


def state(name: str, power: int) -> bool:
    if len(name) > 3 and power > 5:
        return True
    return False


def main() -> None:

    print("Testing spell combiner...")
    combine = spell_combiner(heal, fire)
    print(combine("Dragon", 15))

    print("\nTesting power amplifier...")
    magic = power_amplifier(power_spell, 3)
    print(magic("Dragon", 10))

    print("\nTesting conditional caster...")
    conditional = conditional_caster(state, fire)
    print(conditional("dragon", 12))

    print("\nTesting spell sequence")
    list_functions = [fire, ice_moula, damn_broski]
    maitre_gims = spell_sequence(list_functions)
    print(str(maitre_gims("Stromae", 67)).strip("['']").replace("'", ""))


if __name__ == "__main__":
    main()
