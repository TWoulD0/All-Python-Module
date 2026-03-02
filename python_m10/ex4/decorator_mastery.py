from functools import wraps
import time


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper():
        print(f"Casting {func.__name__}...")

        start = time.time()
        result = func()
        end = time.time()
        time_ = end - start
        print(f"Spell completed in {time_:.3f} seconds")
        return result

    return wrapper


@spell_timer
def fireball():
    time.sleep(0.1)
    return "Fireball cast!"


print(fireball.__name__)


def power_validator(min_power: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def validator(*args, **kw_args):
            power = kw_args.get("power")
            if power is None:
                raise TypeError("Missing power argument")
            if power >= min_power:
                return func(*args, **kw_args)
            return "Insufficient power for this spell"
        return validator
    return decorator


@power_validator(10)
def cast(power: int):
    return f"Sword cast {power}"


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def retry():
            attempts = 0

            while attempts < max_attempts:
                try:
                    func()
                except Exception:
                    attempts += 1
                    print(f"Spell failed, retrying... "
                          f"(attempt {attempts}/{max_attempts})")
            return "Spell casting failed after max_attempts attempts"
        return retry
    return decorator


@retry_spell(5)
def spell():
    raise Exception("error")


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name):
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


def main() -> None:
    print("\nTesting spell timer...")
    print(f"Result: {fireball()}")

    print("\nTesting power validator...")
    print(cast(power=12))

    print("\nTesting retry spell...")
    print(spell())

    print("\nTesting MageGuild...")
    mage = MageGuild()
    print(MageGuild.validate_mage_name("Nova"))
    print(MageGuild.validate_mage_name("No9"))
    print(mage.cast_spell("Lightning", power=15))
    print(mage.cast_spell("flash", power=5))


if __name__ == "__main__":
    main()
