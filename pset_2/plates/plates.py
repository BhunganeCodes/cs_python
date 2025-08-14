def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return two_letters(s) and correct_length(s) and numbers_and_letters(s) and numbers_end(s)

def two_letters(s):
    return 2 <= len(s) and s[0:2].isalpha()

def correct_length(s):
    return 2 <= len(s) <= 6

def numbers_and_letters(s):
    return s.isalnum()

def numbers_end(s):
    number_start = False

    for char in s:
        if char.isdigit():
            if not number_start:
                number_start = True
                if char == "0":
                    return False
        elif number_start:
            return False
    return True

if __name__ == "__main__":
    main()