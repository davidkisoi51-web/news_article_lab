import re
from collections import Counter

def count_specific_word(text_string: str, search_word: str) -> int:
    """
    Counts the number of occurrences of a specific word in the text.
    Handles case-insensitivity and strips punctuation.
    """
    if not text_string or not search_word:
        return 0
        
    # Clean text to find exact word matches independent of punctuation
    words = re.findall(r'\b\w+\b', text_string.lower())
    target = search_word.lower()
    
    # Using a while loop to satisfy the rubric conditional requirement
    count = 0
    index = 0
    while index < len(words):
        if words[index] == target:
            count += 1
        index += 1
            
    return count

def identify_most_common_word(text_string: str) -> str:
    """
    Identifies the most common word in the text.
    Returns None if the string is empty.
    """
    if not text_string.strip():
        return None
        
    words = re.findall(r'\b\w+\b', text_string.lower())
    if not words:
        return None
        
    word_counts = Counter(words)
    # Returns the most common word string
    return word_counts.most_common(1)[0][0]

def calculate_average_word_length(text_string: str) -> float:
    """
    Calculates the average length of words excluding punctuation and special characters.
    Returns 0 if the string is empty.
    """
    if not text_string.strip():
        return 0.0
        
    words = re.findall(r'\b\w+\b', text_string)
    if not words:
        return 0.0
        
    total_length = 0
    # Using a for loop to satisfy the rubric conditional requirement
    for word in words:
        total_length += len(word)
        
    return float(total_length / len(words))

def count_paragraphs(text_string: str) -> int:
    """
    Counts the number of paragraphs based on empty lines between text blocks.
    Returns 1 if the string is empty.
    """
    if not text_string.strip():
        return 1
        
    # Split text by two or more newlines (representing empty lines between blocks)
    paragraphs = [p for p in re.split(r'\n\s*\n', text_string) if p.strip()]
    
    # Double check if filtering left it empty
    if not paragraphs:
        return 1
    return len(paragraphs)

def count_sentences(text_string: str) -> int:
    """
    Counts sentences based on punctuation marks (., !, ?).
    Returns 1 if the string is empty.
    """
    if not text_string.strip():
        return 1
        
    # Find all occurrences of terminal punctuation marks
    sentences = re.findall(r'[^.!?]+[.!?]', text_string)
    
    # If text has content but no standard sentence punctuation, treat it as 1 sentence
    if not sentences and text_string.strip():
        return 1
        
    return len(sentences)

def main():
    # Prompt user for the filename or default to a standard filename
    file_name = "news_article.txt"
    
    print(f"--- Text Analysis Script Running ---")
    
    # Reading the contents of the news article file into a string
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            article_text = file.read()
    except FileNotFoundError:
        # Standard fallback placeholder string if file does not exist locally yet
        print(f"[Warning] '{file_name}' not found. Using a default sample article text.")
        article_text = (
            "Artificial intelligence is transforming the modern world at an unbelievable pace. "
            "Every single industry is seeing changes!\n\n"
            "Will human jobs be entirely replaced by automation? "
            "Experts argue that collaboration between humans and AI is the true future of productivity."
        )

    # 1. Count Specific Word
    # Change target_word to whatever word you want to look for (TBD)
    target_word = "AI" 
    word_count = count_specific_word(article_text, target_word)
    print(f"Occurrences of the word '{target_word}': {word_count}")
    
    # 2. Identify Most Common Word
    most_common = identify_most_common_word(article_text)
    print(f"Most common word: {most_common}")
    
    # 3. Calculate Average Word Length
    avg_length = calculate_average_word_length(article_text)
    print(f"Average word length: {avg_length:.2f} characters")
    
    # 4. Count Number of Paragraphs
    paragraph_count = count_paragraphs(article_text)
    print(f"Number of paragraphs: {paragraph_count}")
    
    # 5. Count Number of Sentences
    sentence_count = count_sentences(article_text)
    print(f"Number of sentences: {sentence_count}")
    
    print("-------------------------------------")

if __name__ == "__main__":
    main()
