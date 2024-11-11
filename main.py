def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()

    num_words = len(text.split())
    print(f"The number of words in the book is: {num_words}")


main()
