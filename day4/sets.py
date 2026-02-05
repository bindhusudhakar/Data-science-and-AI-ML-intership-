raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

unique_users = set(raw_logs)

is_present = "ID05" in unique_users

print("unique_users:", unique_users)
print("Is ID05 present:", is_present)

print("\nCount comparison:")
print("Total log entries:", len(raw_logs))
print("Unique users:", len(unique_users))
