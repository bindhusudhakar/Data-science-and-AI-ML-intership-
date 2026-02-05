contacts = {"Alice": "777-777", "Bob": "555-555", "Charlie": "666-666"}

contacts["Dart"] = "222-222"
contacts["Bob"] = "999-999"

existing_contacts = contacts.get("Alice" , "Contact not found")
missing_contacts = contacts.get("Eve" , "Contact not found")

print("Safe result:")
print("Alice: ", existing_contacts)
print("Eve: ", missing_contacts)

print("\nContacts List:")
for name, phone in contacts.items():
    print(f"Contacts : {name} | Phone : {phone}")
