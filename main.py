from stats import get_book_text_as_string, get_num_words, count_words, count_chars, sort_dict_by_value
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    #print("Example: python main.py books/frankenstein.txt")
    #print("sys.argv[0]: the name of the Python script itself\nsys.argv[1]: the first argument")
    sys.exit(1)

# book1 = "books/frankenstein.txt"
book1 = sys.argv[1]  # Get the book file path from command line arguments

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {get_num_words(book1)} total words")

print("----------- Character Count ----------")
count_chars = count_chars(book1)
for char in count_chars:
    print(f" {char}: {count_chars[char]}")