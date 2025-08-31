from stats import get_num_words, get_num_characters
from sys import argv

def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def main(path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    text = get_book_text(path)
    print(f"Found {get_num_words(text)} total words")
    counts = get_num_characters(text)
    print("----------- Character Count ----------")
    for char, count in counts.items():
        print(f"{char}: {count}")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    main(argv[1])
    exit(0)