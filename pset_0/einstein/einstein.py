def main():
    mass = int(input("mass: ").strip())
    c = 300000000
    E = mass * c ** 2
    print(f"{E:,}")

if __name__ == "__main__":
    main()