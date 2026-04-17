from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def call_spell(*args, **kwargs) -> tuple:
        res1 = spell1(*args, **kwargs)
        res2 = spell2(*args, **kwargs)
        return (res1, res2)

    return call_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def power_magic(*args, **kwargs):
        res1 = multiplier * base_spell(*args, **kwargs)
        return res1

    return power_magic


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(*args, **kwargs):
        if state(spell):
            return spell(*args, **kwargs)
        return "spell fizzled"

    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_all(*args, **kwargs):
        res_list = []
        for spell in spells:
            res_list.append(spell(*args, **kwargs))
        return res_list

    return cast_all


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def power(power: int):
    return power


def fire(target: str, power: int) -> str:
    return f"{target} has {power} fire"


def ice_moula(target: str, power: int) -> str:
    return f"{target} made a lot of {power}"


def damn_broski(target: str, power: int) -> str:
    return f"Damn the fendi suits you well {target}, you have {power} moula "


def state(func: Callable) -> bool:
    return func is fire


def main():

    print("Testing spell combiner...")
    combine = spell_combiner(heal, fire)
    print(combine("Dragon", 15))

    print("\nTesting power amplifier...")
    magic = power_amplifier(power, 3)
    print(f"Original: 3, Amplified: {magic(5)}")

    print("\nTesting conditional caster...")
    conditional = conditional_caster(state, fire)
    print(conditional("dragon", 14))

    print("\nTesting spell sequence")
    list_functions = [fire, ice_moula, damn_broski]
    maitre_gims = spell_sequence(list_functions)
    print(str(maitre_gims("Stromae", 67)).strip("['']").replace("'", ""))


if __name__ == "__main__":
    main()
