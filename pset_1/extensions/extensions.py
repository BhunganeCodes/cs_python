def main():
    filename = input("File name: ").strip().lower()
    parts = filename.split(".")
    extension = parts[-1]

    match extension:
        case "jpeg" | "jpg":
            print("image/jpeg")
        case "gif" | "png":
            print(f"image/{extension}")
        case "pdf" | "zip":
            print(f"application/{extension}")
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")

if __name__ == "__main__":
    main()