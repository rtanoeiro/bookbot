def count_characters(text: str) -> dict[str, int]:
    character_dictionary = {}

    for character in text:
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1

    return character_dictionary


def main():
    with open("books/frankenstein.txt") as f:
        text = (f.read()).lower()
        num_words = len(text.split())
        char_count = count_characters(text)

    print(f"The number of words in the book is: {num_words}")
    print(f"The character dictionary for the text is: {char_count}")


main()
