def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    count_words = get_count_words(text)
    print(f"Total words: {count_words}")
    lett = get_count_letters(text)
    print(f"Total letters: {lett}")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_count_words(text):
    words = text.split()
    return len(words)


def get_count_letters(text):
    text = text.lower()
    letters = dict()
    for letter in text:
        if letter.isalpha():
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters


main()
