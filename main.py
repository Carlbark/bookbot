from stats import count_words


def get_book_text(filepath):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        filepath (str): The relative path to the book file.
       
    Returns:
        str: The content of the book.
    """
    try:
        with open(filepath) as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"
    



def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book_text(book_path)
    num_words = count_words(book_content)
    print(f"{num_words} words found in the document")

main()