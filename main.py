from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def print_report(book_path, num_words, sorted_char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in range(len(sorted_char_list)):
        print(': '.join(map(str,sorted_char_list[item])))
    print("============= END ===============")

'''
def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
'''

def main():
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path) 
    num_words = get_word_count(text)
    letter_count = get_char_count(text)
    sorted_char_list = get_sorted_char(letter_count)

    print_report(book_path, num_words, sorted_char_list)
         

if __name__ == '__main__':
    main()
    