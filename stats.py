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
