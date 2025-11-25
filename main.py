from stats import count_words
from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()



def main():
    #print(get_book_text("books/frankenstein.txt"))
    if len(sys.argv) >=2:
        path=sys.argv[1]
        words= count_words(get_book_text(path))
        #print(f"Found {words} total words")
        chars={}
        chars=count_chars(get_book_text(path))
        #print(chars)
        header= "============ BOOKBOT ============"
        print(header)
        header2=f"Analyzing book found at {path}..."
        print(header2)
        header3="----------- Word Count ----------"
        print(header3)
        print(f"Found {words} total words")
        header4="--------- Character Count -------"
        print(header4)
        sorted_dict=sort_dict(chars)
        for dict in sorted_dict:
            print(f"{dict["char"]}: {dict["num"]}")
        header5="============= END ==============="
        print(header5)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
main()