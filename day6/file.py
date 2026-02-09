name = input("Enter your Name: ")
goal = input("Enter your Daily Goal: ")

with open("day6/journel.txt","a") as file:
    file.write(f"Name: {name} , Daily Goal: {goal}\n")

print("Saved Successfully")
