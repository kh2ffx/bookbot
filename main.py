#!/usr/bin/env python3

from stats import num_words
from stats import num_char
from stats import report_sort
import sys


def get_book_text(path_to_book):
    with open(path_to_book) as book:
        book_contents = book.read()
    return book_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)   
    
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------\nFound {num_words(get_book_text(sys.argv[1]))} total words\n--------- Character Count -------")
    for dictionary in report_sort(num_char(get_book_text(sys.argv[1]))):
          print(f"{dictionary["char"]}: {dictionary["num"]}") 
    print(f"============= END ===============")

main()

