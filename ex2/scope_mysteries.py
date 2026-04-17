from typing import Any
from collections.abc import Callable


def mage_counter() -> Callable:
    call_number = 0

    def count() -> int:
        nonlocal call_number
        call_number += 1
        return call_number

    return count


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def memory(power_to_add: int) -> int:
        nonlocal total_power
        total_power += power_to_add
        return total_power

    return memory


def enchantment_factory(enchantment_type: str) -> Callable:
    def apply_enchant(item: str) -> str:
        return f"{enchantment_type} {item}"

    return apply_enchant


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, Any] = {}

    def store(key: str, value: Any) -> str:
        memory.update({key: value})
        return f"Store '{key}' - {value}"

    def recall(key: str) -> Any:
        if memory.get(key) is None:
            return "Memory not found"
        return f"Recall '{key}' : {memory.get(key)}"

    dictio: dict[str, Callable] = {"store": store, "recall": recall}
    return dictio


def main() -> None:
    print("Testing mage counter...")
    count1 = mage_counter()
    count2 = mage_counter()
    print("counter_one")
    for i in range(3):
        print(f"counter_one call {i+1}: {count1()}")
    print("counter_two")
    for i in range(3):
        print(f"counter_one call {i+1}: {count2()}")

    print("\nTesting spell accumulator...")
    power_acc = spell_accumulator(100)
    print(f"Base 100, add 200 : {power_acc(200)}")
    print(f"Base 100, add 25 : {power_acc(25)}")

    print("\nTesting enchantment factory...")
    enchant = enchantment_factory("swollen")
    print(enchant("shield"))
    enchant = enchantment_factory("super")
    print(enchant("sword"))

    print("\nTesting memory vault...")
    pub_dic = memory_vault()
    print(pub_dic["store"]("secret", "42"))
    print(pub_dic["recall"]("secret"))
    print(pub_dic["recall"]("ali"))


if __name__ == "__main__":
    main()
