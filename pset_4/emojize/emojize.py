import emoji

def main():
    emoji_str = input("Input: ").strip().lower()
    print(f"Output: {emoji.emojize(emoji_str, language='alias')}")

if __name__ == "__main__":
    main()