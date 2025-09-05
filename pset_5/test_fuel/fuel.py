def main():
    try:
        fraction = input("Enter your fuel fraction: ").strip()
        percentage = convert(fraction)
        print(gauge(percentage))

    except (ValueError, ZeroDivisionError):
        print("Error: Incorrect Usage")


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x, y = int(x), int(y)

        if x > y:
            raise ValueError
        if y == 0:
            raise ZeroDivisionError
        if x < 0 and y < 0:
            raise ValueError
        
        return round(x / y * 100)
    except (ValueError, ZeroDivisionError):
        raise
    


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()