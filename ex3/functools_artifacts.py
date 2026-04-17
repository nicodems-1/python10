from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if spells:
        dict = {
            "add": lambda x, y: add(x, y),
            "multiply": lambda x, y: mul(x, y),
            "max": lambda x, y: max(x, y),
            "min": lambda x, y: min(x, y),
        }
        return reduce(dict[operation], spells)
    return 0


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    first: Callable = partial(base_enchantment, 50, "fire")
    second: Callable = partial(base_enchantment, 50, "ice")
    third: Callable = partial(base_enchantment, 50, "water")
    all_func = {"first": first, "second": second, "third": third}
    return all_func


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{target} received {power} of {element}"


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def base_spell(argument: Any):
        return "Unknown spell type"

    @base_spell.register
    def _(argument: int):
        return f"Damage spell: {argument} damage"

    @base_spell.register
    def _(argument: str):
        return f"Enchantments: {argument}"

    @base_spell.register
    def _(argument: list):
        return f"Multi-cast: {len(argument)}"

    return base_spell


def main():
    spells = [1, 54, 45, 152]
    try:
        print(spell_reducer(spells, "add"))
    except KeyError as e:
        print(
            f"No operation: {e} available, "
            f"try 'max', 'min', 'multiply' or 'add' instead"
        )
    try:
        func_dict = partial_enchanter(base_enchantment)
        print(func_dict["first"]("sword"))
        print(func_dict["second"]("shield"))
        print(func_dict["third"]("arc"))
    except KeyError as e:
        print(f"missing key : {e} in func dict")

    print(memoized_fibonacci(10))
    print(memoized_fibonacci(15))

    base_spell = spell_dispatcher()
    print(base_spell(10))
    print(base_spell("patapouf"))
    print(base_spell(["lala", "toto", "ziguigui"]))
    print(base_spell({"key": "value"}))


if __name__ == "__main__":
    main()
