def count_words(text):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())

def count_character_statistics(text):
    """
    Counts the number of characters in a given text.
    
    Args:
        text (str): The text to count characters in.
        
    Returns:
        dict: A dictionary of each character and the number of times
        it occurs. Uppercase will be converted and counted as lowercase.
    """
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():  # Count only alphabetic characters
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

def sort_dictionary_by_count(char_dict):
    """
    Sorts a character count dictionary by the count of characters.
    
    Args:
        char_dict (dict): The dictionary to sort.
        
    Returns:
        list: A sorted list of dictionaries, each containing two key-value pairs:
        one for the character itself and one for its count.
    """
    def get_count(item):
        # item is a tuple (char, count)
        return item[1]

    items = list(char_dict.items())  # Convert dictionary to list of key-value pairs
    items.sort(key=get_count, reverse=True)

    result = []
    for char, count in items:
        result.append({"char": char, "num": count})
    return result
