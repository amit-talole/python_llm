student = {"name": "Amit", "age": 25, "city": "Delhi"}

# using key
print(student["name"])   # Amit

# using get() — safer if key may be missing
print(student.get("age"))           # 25
print(student.get("email"))         # None (no error)
print(student.get("email", "N/A"))  # N/A (default value)

# student["email"]  # KeyError if key does not exist
