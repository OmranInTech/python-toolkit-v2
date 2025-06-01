import json
import os
from cryptography.fernet import Fernet
from getpass import getpass

class PasswordManager:
    def __init__(self, key_file="key.key", data_file="passwords.json"):
        self.key_file = key_file
        self.data_file = data_file
        self.key = self.load_or_generate_key()
        self.cipher_suite = Fernet(self.key)

    def load_or_generate_key(self):
        """Load existing key or generate a new one."""
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as file:
                return file.read()
        key = Fernet.generate_key()
        with open(self.key_file, "wb") as file:
            file.write(key)
        return key

    def load_passwords(self):
        """Load saved passwords."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("⚠️ Warning: Password file is corrupted. Starting fresh.")
                return {}
        return {}

    def save_passwords(self, passwords):
        """Save encrypted passwords."""
        with open(self.data_file, "w") as file:
            json.dump(passwords, file)

    def encrypt_password(self, password):
        return self.cipher_suite.encrypt(password.encode()).decode()

    def decrypt_password(self, encrypted_password):
        return self.cipher_suite.decrypt(encrypted_password.encode()).decode()

    def add_password(self, service, password):
        passwords = self.load_passwords()
        if service in passwords:
            confirm = input(f"⚠️ Password for '{service}' already exists. Overwrite? (y/n): ").strip().lower()
            if confirm != "y":
                print("Operation cancelled.")
                return
        encrypted = self.encrypt_password(password)
        passwords[service] = encrypted
        self.save_passwords(passwords)
        print(f"✅ Password for '{service}' saved successfully!")

    def get_password(self, service):
        passwords = self.load_passwords()
        if service in passwords:
            return self.decrypt_password(passwords[service])
        print("❌ No password found for this service.")
        return None

    def list_passwords(self):
        passwords = self.load_passwords()
        if not passwords:
            print("📭 No passwords stored.")
            return
        print("\nStored Passwords:")
        print("-" * 30)
        for service, encrypted in passwords.items():
            try:
                decrypted = self.decrypt_password(encrypted)
                print(f"{service}: {decrypted}")
            except Exception:
                print(f"{service}: ❌ Failed to decrypt.")
        print("-" * 30)


def main():
    pm = PasswordManager()
    
    while True:
        print("\n🔐 Password Manager")
        print("1️⃣  Add a password")
        print("2️⃣  Retrieve a password")
        print("3️⃣  List all passwords")
        print("4️⃣  Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            service = input("Enter service name: ").strip()
            password = getpass("Enter password (input hidden): ").strip()
            pm.add_password(service, password)

        elif choice == "2":
            service = input("Enter service name: ").strip()
            password = pm.get_password(service)
            if password:
                print(f"🔑 Password for '{service}': {password}")

        elif choice == "3":
            pm.list_passwords()

        elif choice == "4":
            print("👋 Exiting Password Manager.")
            break

        else:
            print("❌ Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
