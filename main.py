from stats import count_characters, count_words


def create_book_report(book_path: str) -> None:
    with open(book_path) as f:
        text = (f.read()).lower()

    num_words = count_words(text)
    print(f"{num_words} words found in the document")


def main():
    print("--- Begin report ---")
    create_book_report("books/frankenstein.txt")
    print("--- End report ---")


main()
