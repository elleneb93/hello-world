def print_hello():
    print("Hello world")

def add_one(number):
    return number + 1

print_hello()
eight_plus_one = add_one(8)
print(eight_plus_one)

instructors = ["Darren", "Nina", "Simon"]
print(f"The second instructor in the list is {instructors[1]}")

member = {"name": "Darren", "favourite_language": "Python"}
for key, value in member.items():
  # replaces underscores with spaces so it reads nicer
  key = key.replace("_", " ")

  print(f"The member's {key} is {value}.")
