def main():
    book_path = "books/frankenstein.txt"
    text = get_books_text(book_path)
    len_tex = split_text(text)
    print(f"========== Begin report of {book_path} ==========")
    print(f"{len_tex} words found in the document")
    print("")
    dict_of_symbols(text)

def get_books_text(path):
    with open(path) as f:
        file_contents = f.read()
        return(file_contents)
    
def split_text(text):
    words = text.split()
    return(len(words))

def dict_of_symbols(text):
    new_dict = {}
    for symbol in list(text.lower()):
        if (symbol.isalpha()):
            if (symbol in new_dict):
                new_dict[symbol] += 1
            else:
                new_dict[symbol] = 1
    for s in sorted(new_dict.items(), key = lambda para: (para[0], para[1])):
        print(f"The '{s[0]}' character was found {s[1]} times")

    
main()
