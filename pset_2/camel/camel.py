def main():
    camel = input("camelCase: ").strip()
    snake = ""

    for letter in camel:
        if letter.isupper():
            snake += "_" + letter.lower()
        else:
            snake += letter
    print(f"snake_case: {snake}")


if __name__ == "__main__":
    main()