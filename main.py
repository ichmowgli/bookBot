def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words = get_count_words(text)
    letters = get_count_letters(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words} words found in the document\n")

    for letter, num in letters.items():
        print(f"The '{letter}' character was found {num} times")

    print(f"--- End report ---")


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


def sort_on(d):
    return d["num"]


def get_sorted_letters(letters):
    sorted_letters = sorted(letters.items(), key=sort_on, reverse=True)
    return sorted_letters


main()
