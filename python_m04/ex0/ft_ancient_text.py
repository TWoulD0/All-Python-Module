
print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

filename = "ancient_fragment.txt"
print(f"Accessing Storage Vault: {filename}")

try:
    file = open(filename, "r")

    print("Connection established...")
    print("\nRECOVERED DATA:")

    content = file.read()
    print(content)
    file.close()

    print("\nData recovery complete. Storage unit disconnected.")

except FileNotFoundError as e:
    print(f"Error: {e}")
