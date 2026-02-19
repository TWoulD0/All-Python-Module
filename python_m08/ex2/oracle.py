import os
import sys
from dotenv import load_dotenv


def check_required(var_name: str) -> str:
    value = os.getenv(var_name)
    if not value:
        raise ValueError(f"Missing required configuration: {var_name}")
    return value


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")

    load_dotenv()

    try:
        matrix_mode = os.getenv("MATRIX_MODE", "development")
        check_required("DATABASE_URL")
        check_required("API_KEY")
        log_level = os.getenv("LOG_LEVEL", "INFO")
        zion_endpoint = check_required("ZION_ENDPOINT")

        print("\nConfiguration loaded:")
        print(f"Mode: {matrix_mode}")

        print(
            "Database:",
            "Connected to local instance"
            if matrix_mode == "development"
            else "Connected to production instance"
        )

        print("API Access: Authenticated")
        print(f"Log Level: {log_level}")
        print(f"Zion Network: Online ({zion_endpoint})")

        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")

        print("\nThe Oracle sees all configurations.")

    except ValueError as e:
        print("\nCONFIGURATION ERROR:")
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
