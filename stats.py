# stats.py

def get_book_text_as_string(file_path):
    # utf-8 encoding is for linux/mac, cp1252 is for windows
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()  # read entire file as a string
        return(file_content)

def get_num_words(file_path):
    words = get_book_text_as_string(file_path)
    words_count = len(words.split())
    return words_count

def count_words(file_path):
    dict = {}
    words = get_book_text_as_string(file_path)
    words = words.lower()  # convert to lowercase for case-insensitive counting
    words = words.split()
    for word in words:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    return dict

def sort_dict_by_value(d):
    # sorts a dictionary by its values in descending order
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

def count_chars(file_path):
    # counts the number of occurrences of each character in the book
    dict = {}
    words = get_book_text_as_string(file_path)
    words = words.lower()
    
    for char in words:
        if char.isalpha():
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] +=1
    # sort_dict_by_value(dict) # error, b/c forgot to catch the output of it
    return sort_dict_by_value(dict)  # sort the dictionary by value in descending order

