from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Any
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    try:
        if spells:
            dict = {
                "add": lambda x, y: add(x, y),
                "multiply": lambda x, y: mul(x, y),
                "max": lambda x, y: max(x, y),
                "min": lambda x, y: min(x, y),
            }
            return reduce(dict[operation], spells)
        return 0
    except KeyError as e:
        print(
            f"No operation: {e} available, "
            f"try 'max', 'min', 'multiply' or 'add' instead"
        )
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
        return f"Enchantments: {argument} "

    @base_spell.register
    def _(argument: list):
        return f"Multi-cast: {len(argument)} spells"

    return base_spell


def main():
    spells = [1, 54, 45, 152]
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting partial_enchanter...")
    try:
        func_dict = partial_enchanter(base_enchantment)
        print(func_dict["first"]("sword"))
        print(func_dict["second"]("shield"))
        print(func_dict["third"]("arc"))
    except KeyError as e:
        print(f"missing key : {e} in func dict")

    print("\nTesting spell dispatcher...")
    base_spell = spell_dispatcher()
    print(base_spell(10))
    print(base_spell("patapouf"))
    print(base_spell(["lala", "toto", "ziguigui"]))
    print(base_spell({"key": "value"}))


if __name__ == "__main__":
    main()
