def main():
    answer = input("What is the answer to the Great Universal Question? ").lower().strip()

    match answer:
        case "forty two" | "forty-two" | "42":
            print("Yes")
        case _:
            print("No")

if __name__ == "__main__":
    main()