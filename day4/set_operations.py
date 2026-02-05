friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}

shared_interests = friend_a & friend_b
all_interests = friend_a | friend_b
unique_to_a = friend_a - friend_b

print("Shared interets: ", shared_interests)
print("All interests: ", all_interests)
print("Only friend a interests: ", unique_to_a)