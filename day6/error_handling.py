filename = input("Enter the filename to open: ")

try:
    file = open("day6/config.txt", "r")
    content = file.read()
    print("\nFile contents:\n")
    print(content)

except FileNotFoundError:
    print("Oops! That file doesn't exist yet ")