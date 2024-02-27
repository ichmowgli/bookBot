def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    count_words = get_count_words(text)
    print(f"Total words: {count_words}")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_count_words(text):
    words = text.split()
    return len(words)


main()
