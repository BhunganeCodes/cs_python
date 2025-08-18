def main():
    while True:
        try:
            date = input("Date: ").strip().capitalize()

            if "/" in date:
                month, day, year = date.split("/")
                month, day, year = int(month), int(day), int(year)
            
            elif "," in date:
                month_str, day_year = date.split(" ", 1)
                day, year = day_year.replace(",", "").split()
                day, year = int(day), int(year)

                months = [
                    "January",
                    "February",
                    "March",
                    "April",
                    "May",
                    "June",
                    "July",
                    "August",
                    "September",
                    "October",
                    "November",
                    "December"
                ]

                if month_str not in months:
                    continue
                month = months.index(month_str) + 1
            else:
                continue
                
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break

        except ValueError:
            continue

if __name__ == "__main__":
    main()