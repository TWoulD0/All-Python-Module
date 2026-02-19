import sys
import os
import site


def is_in_env() -> bool:
    try:
        if sys.prefix != sys.base_prefix or "VIRTUAL_ENV" in os.environ:
            return True
        else:
            return False
    except Exception:
        if "VIRTUAL_ENV" in os.environ:
            return True
        else:
            return False


def venv_name_path() -> tuple[str, str]:
    try:
        venv_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
        venv_name = os.path.basename(os.path.normpath(venv_path)) or "Unknown"
        return venv_name, venv_path
    except Exception:
        return "Unknown", sys.prefix


def get_site_packages_path() -> str:
    try:
        paths = site.getsitepackages()
        if isinstance(paths, list) and paths:
            return paths[0]
        return "site-packages not found"
    except Exception:
        try:
            user_site = site.getusersitepackages()
            return user_site or "user site-packages not found"
        except Exception:
            return "site-packages not accessible"


def print_outside_env() -> None:
    print("\nMATRIX STATUS: You're still plugged in")

    # sys.executable = give you a path of what version of python
    # this script is working on
    print(f"\nCurrent Python: {sys.executable}")
    print("Virtual Environment: None detected")

    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")


def print_inside_env() -> None:
    name, path = venv_name_path()
    print("\nMATRIX STATUS: Welcome to the construct")

    print(f"\nCurrent Python: {sys.executable}")
    print(f"Virtual Environment: {name}")
    print(f"Environment Path: {path}")

    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")

    print("Package installation path:")
    print(get_site_packages_path())


def main() -> None:
    try:
        if is_in_env():
            print_inside_env()
        else:
            print_outside_env()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
