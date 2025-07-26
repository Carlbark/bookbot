from stats import count_words, count_character_statistics, sort_dictionary_by_count


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