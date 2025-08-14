def main():
    try:
        expression = input("Expression: ").strip()
        print(float(eval(expression)))
    except:
        print("Error: Invalid entry")
if __name__ == "__main__":
    main()