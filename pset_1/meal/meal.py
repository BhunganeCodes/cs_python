def main():
    time = input("Time: ").strip()
    converted_time = convert(time)

    try:
        if 7 <= converted_time <= 8:
            print("Breakfast")
        elif 12 <= converted_time <= 13:
            print("Lunch")
        elif 18 <= converted_time <= 19:
            print("Dinner")
    except:
        pass
    
def convert(time):
    try:
        hours, mins = time.split(":")
        return float(hours) + float(mins) / 60
    except:
        pass

if __name__ == "__main__":
    main()