def main():
    plate = input("Enter your plate: ").strip()
    if is_valid(plate):
        print("Valid!")
    else:
        print("Invalid!")


def is_valid(s):
    return two_letters(s) and correct_length(s) and letters_and_numbers(s) and numbers_end(s)

def two_letters(s):
    return len(s) >= 2 and s[0:2].isalpha()

def correct_length(s):
    return 2 <= len(s) <= 6

def letters_and_numbers(s):
    return s.isalnum()

def numbers_end(s):
    numbers_start = False

    for char in s:
        if char.isdigit():
            if not numbers_start:
                numbers_start = True
                if char == "0":
                    return False
        elif numbers_start:
            return False
    return True


if __name__ == "__main__":
    main()