from typing import Callable
import time
from functools import wraps
import random


def spell_timer(func: Callable):
    depth = 0

    @wraps(func)
    def my_timer_wrapper(*args, **kwargs):
        nonlocal depth
        if depth == 0:
            print(f"Casting {func.__name__}")
            start_time = time.perf_counter()
            depth += 1
            result = func(*args, **kwargs)
            depth -= 1
            end_time = time.perf_counter()
            total_time = end_time - start_time
            print(f"Spell completed in {round(total_time, 3)} seconds")
            return result
        else:
            return func(*args, **kwargs)

    return my_timer_wrapper


@spell_timer
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fibonacci(n - 1) + fibonacci(n - 2)


def power_validator(min_power: int) -> Callable:
    def wrapper(func: Callable):
        @wraps(func)
        def power_validator_wrap(*args, **kwargs):
            if len(args) == 1:
                power = args[0]
            else:
                power = args[2]
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"

        return power_validator_wrap

    return wrapper


def retry_spell(max_attempts: int) -> Callable:
    def wrapper(func: Callable):
        @wraps(func)
        def retry_spell_wrap(*args, **kwargs):
            for i in range(max_attempts):
                try:
                    return func()
                except Exception:
                    print(
                        f"Spell failed, retrying..."
                        f"(attempt {i+1}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"

        return retry_spell_wrap

    return wrapper


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and (name.isalpha() or name == " ")

    @power_validator(10)
    def cast_spell(self, spell_name, power):
        return f"Successfully cast {spell_name} with {power} power"


@retry_spell(5)
def failed_spell():
    if random.randint(0, 5) != 5:
        raise ValueError
    return "YES"


@power_validator(5)
def power_spell(power: int):
    if power:
        return "Waaaaaaaaagh spelled"


if __name__ == "__main__":
    print(fibonacci(20))
    print(power_spell(6))
    print(failed_spell())
    the_mage = MageGuild()
    print(the_mage.validate_mage_name("Michel"))
    print(the_mage.cast_spell("firewater", 4))
