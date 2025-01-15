# sample_script.py
def greet(name: str) -> str:
    """
    Return a greeting message for the given name.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message.
    """
    if not name:
        raise ValueError("Name cannot be empty.")
    return f"Hello, {name}!"


if __name__ == "__main__":
    try:
        name_input = input("Enter your name: ")
        print(greet(name_input))
    except ValueError as e:
        print(f"Error: {e}")
