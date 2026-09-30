def validate_input(user_input):
    if not user_input.strip():
        return "Invalid input"
    return "Valid input"


name = input("Enter your name: ")
print(validate_input(name))