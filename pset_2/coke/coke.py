def main():
    coins = [25, 10, 5]
    due = 50
    while True:
        print(f"Amount Due: {due}")
        inserted = int(input("Insert Coin: "))

        if inserted in coins:
            due -= inserted
        else:
            continue
        if due <= 0:
            print(f"Changed Owed: {abs(due)}")
            break

if __name__ == "__main__":
    main()