def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    # Lowercase text and remove whitespaces
    text = text.lower().strip()
    # Count characters using a dictionary
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
        