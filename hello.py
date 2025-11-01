def main():
    name = input("Enter your name: ")
    print(greet(name))

# custom greeting function
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    main()