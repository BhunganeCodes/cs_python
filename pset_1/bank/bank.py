def main():
    greet = input("Greeting: ").lower().strip()
    print(f"${convert(greet)}")

def convert(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()