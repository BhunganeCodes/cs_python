def main():
    expression = input("Expression: ").strip()
    vowels = "aeiouAEIOU"
    clean = ""

    for char in expression:
        if char not in vowels:
            clean += char
    print(f"Output: {clean}")


if __name__ == "__main__":
    main()