def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_list = sorted(artifacts, key=lambda x: x["power"], reverse=True)
    return sorted_list


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    powerful_mages = filter(lambda mage: mage["power"] >= min_power, mages)
    return list(powerful_mages)


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x["power"])
    min_power = min(mages, key=lambda x: x["power"])
    avg_power = round(sum(map(lambda x: x["power"], mages)) / len(mages), 2)
    return {
        "max_power": max_power["power"],
        "min_power": min_power["power"],
        "avg_power": avg_power,
    }


if __name__ == "__main__":
    artifacts = [
        {"name": "Wind Cloak", "power": 61, "type": "armor"},
        {"name": "Wind Cloak", "power": 92, "type": "focus"},
        {"name": "Light Prism", "power": 80, "type": "focus"},
        {"name": "Water Chalice", "power": 65, "type": "focus"},
    ]
    print("Testing artifact sorter...")
    print(artifact_sorter(artifacts))
    print()
    mages = [
        {"name": "Casey", "power": 94, "element": "wind"},
        {"name": "Nova", "power": 73, "element": "shadow"},
        {"name": "Ember", "power": 62, "element": "ice"},
        {"name": "River", "power": 98, "element": "lightning"},
        {"name": "Kai", "power": 81, "element": "lightning"},
    ]
    print("Testing power filter mage, power >= 85")
    print(power_filter(mages, 85))
    spells = ["tornado", "lightning", "shield", "fireball"]
    print()
    print("Testing spell transformer...")
    print(" ".join(spell_transformer(spells)))
    print()
    print("Testing mage_stats")
    print(mage_stats(mages))
