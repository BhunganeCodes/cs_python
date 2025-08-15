def main():
    while True:
        try:
            fuel = input("Fraction: ").strip()
            percentage = convert(fuel)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
    try:
        x, y = fraction.split("/")
        x, y = int(x), int(y)

        if x > y:
            raise ValueError
        if y == 0:
            raise ZeroDivisionError
        if x < 0 or y < 0:
            raise ValueError

        return round((x / y) * 100)

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