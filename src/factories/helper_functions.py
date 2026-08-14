def view_character_model():
    for section in fields(Character):

        field_type = section.type

        try:
            subfields = fields(field_type)
            print(f"\n{section.name}:")
            for value in subfields:
                print(f"  - {value.name}")
        except TypeError:
            print(f"\n{section.name}: {field_type}")

def get_int_input(prompt: str, min_val: int = None, max_val: int = None) -> int:
    """Allows an int input to have constraints"""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be smaller than {max_val}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

def get_bool_input(prompt: str)-> bool:
    """Validates Yes/No from user."""
    while True:
        response = input(f"{prompt} (y/n)").lower().strip()
        if response in ['y', 'yes']:
            return True
        elif response in ['n','no']:
            return False
        else:
            print("Please enter 'y' or 'n'.")

def get_choice_input(prompt: str, options: list) -> int:
    """Displays options as a list to allow the user to pick easily"""
    print(f"\n{prompt}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        choice = get_int_input("Enter your choice: ", 1, len(options))
        return choice -1