def count_characters(text: str) -> dict[str, int]:
    character_dictionary = {}

    for character in text:
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1

    return character_dictionary


def create_book_report(char_dict: dict[str, int]) -> None:
    for char, value in char_dict.items():
        print(f"The '{char}' character was found {value} times")


def main():
    with open("books/frankenstein.txt") as f:
        text = (f.read()).lower()
        char_count = count_characters(text)

    print(f"--- Begin report of {f.name} ---")
    create_book_report(char_dict=char_count)


main()
