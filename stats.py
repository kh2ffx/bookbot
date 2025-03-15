def num_words(book_text):
    words = book_text.split()
    return len(words)

def num_char(book_text):
    fixed_text = book_text.lower()
    char_count = {}
    for char in fixed_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count 


def sort_on(dict):
    return dict["num"]

def report_sort(char_count):
    dict_list = []

    for key in char_count:
        if key.isalpha():
            new_dict = {}
            new_dict["char"] = key
            new_dict["num"] = char_count[key]
            dict_list.append(new_dict)
#    print(dict_list)

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list 
