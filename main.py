from stats import count_characters, count_words
import sys


def get_word_count(book_path: str) -> int:
    with open(book_path) as f:
        text = (f.read()).lower()

    return count_words(text)


def get_character_count(book_path: str) -> dict[str, int]:
    with open(book_path) as f:
        text = (f.read()).lower()

    return count_characters(text)


def main(file_path):
    num_words = get_word_count(file_path)
    character_dict = get_character_count(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character, count in character_dict.items():
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
