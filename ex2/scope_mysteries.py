from typing import Callable, Any


def mage_counter() -> Callable:
    call_number = 0

    def count() -> int:
        nonlocal call_number
        call_number += 1
        return call_number

    return count


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def memory(*args, **kwargs) -> int:
        nonlocal total_power
        total_power += args[0]
        return total_power

    return memory


def enchantment_factory(enchantment_type: str) -> Callable:
    def apply_enchant(*args, **kwargs) -> str:
        return f"{enchantment_type} {args[0]}"

    return apply_enchant


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(*args, **kwargs) -> str:
        memory.update({args[0]: args[1]})
        return f"Store '{args[0]}' - {args[1]}"

    def recall(*args, **kwargs) -> Any:
        if memory.get(args[0]) is None:
            return "Memory not found"
        return f"Recall '{args[0]}' : {memory.get(args[0])}"

    dictio = {"store": store, "recall": recall}
    return dictio


def main():
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
