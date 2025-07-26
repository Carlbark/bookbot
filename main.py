from stats import count_words, count_character_statistics, sort_dictionary_by_count
import sys

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
        raise FileNotFoundError(f"File '{filepath}' not found.")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    try:
        book_content = get_book_text(book_path)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    num_words = count_words(book_content)
    char_dict = count_character_statistics(book_content)
    sorted_list = sort_dictionary_by_count(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")  
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()