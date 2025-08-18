def main():
    grocery_list = {}

    while True:
        try:
            item = input("Item: ").lower().strip()
            if item:
                if item in grocery_list:
                    grocery_list[item] += 1
                else:
                    grocery_list[item] = 1
            elif item == "":
                continue

        except (EOFError, KeyError):
            print()
            break

    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item.upper()}")

if __name__ == "__main__":
    main()