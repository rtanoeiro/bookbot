def count_characters(text: str) -> dict[str, int]:
    character_dictionary = {}

    for character in text:
        if character in (" ", "\n"):
            continue
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1

    sorted_char = sorted(character_dictionary.items(), key=lambda x: x[1], reverse=True)
    sorted_char_dict = dict(sorted_char)

    return sorted_char_dict


def count_words(text: str) -> int:
    return len(text.split())
