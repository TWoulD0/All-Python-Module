
def crisis_alerts(file_name):
    if file_name == "standard_archive.txt":
        print(f"\nROUTINE ACCESS: Attempting access to '{file_name}'...")
    else:
        print(f"\nCRISIS ALERT: Attempting access to '{file_name}'...")

    try:
        with open(file_name, "r") as file:
            content = file.read()
            print(f"SUCCESS: Archive recovered - ''{content}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")


def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    crisis_alerts("lost_archive.txt")
    crisis_alerts("classified_vault.txt")
    crisis_alerts("standard_archive.txt")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


main()
