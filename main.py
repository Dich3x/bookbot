def main():
    book_path = "books/frankenstein.txt"
    text = get_books_text(book_path)
    print(text)
    len_tex = split_text(text)
    print(f"words in text {len_tex}")

def get_books_text(path):
    with open(path) as f:
        file_contents = f.read()
        return(file_contents)
    
def split_text(text):
    words = text.split()
    return(len(words))
main()
