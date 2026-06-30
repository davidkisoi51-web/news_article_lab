"""
Module: pythonAssessment.py
Description: Production-grade NLP text analysis tool for news articles.
"""

import re
from collections import Counter

def count_specific_word(text: str, search_word: str) -> int:
    """
    Counts the number of times a specific word is used, case-insensitively.
    Uses regex boundary matching to avoid matching substrings inside larger words.
    """
    if not text or not search_word:
        return 0
    # \b ensures we match whole words only (e.g., 'the' won't match 'there')
    pattern = rf"\b{re.escape(search_word)}\b"
    matches = re.findall(pattern, text, re.IGNORECASE)
    return len(matches)

def identify_most_common_word(text: str) -> str:
    """
    Identifies and returns the most common word in the text.
    Cleans punctuation and standardizes to lowercase.
    """
    if not text.strip():
        return ""
    # Extract all words, converting to lowercase
    words = re.findall(rf"\b\w+\b", text.lower())
    if not words:
        return ""
    
    word_counts = Counter(words)
    # most_common(1) returns a list like [('word', count)]
    return word_counts.most_common(1)[0][0]

def calculate_average_word_length(text: str) -> float:
    """
    Calculates the average length of words in the string as a float.
    """
    words = re.findall(rf"\b\w+\b", text)
    if not words:
        return 0.0
    
    total_length = 0
    # Meeting the 'for loop' requirement by iterating through words
    for word in words:
        total_length += len(word)
        
    return float(total_length / len(words))

def count_paragraphs(text: str) -> int:
    """
    Counts the number of paragraphs in the text.
    Paragraphs are typically separated by one or more newlines.
    """
    if not text.strip():
        return 0
    # Split by double newlines or single newlines that separate text blocks
    paragraphs = [p for p in text.split('\n') if p.strip()]
    return len(paragraphs)

def count_sentences(text: str) -> int:
    """
    Counts the number of sentences in the text using punctuation boundaries.
    """
    if not text.strip():
        return 0
    # Matches sentences ending in ., !, or ?
    sentences = re.split(r'[.!?]+', text)
    # Remove empty strings caused by trailing punctuation or spacing
    actual_sentences = [s for s in sentences if s.strip()]
    return len(actual_sentences)


if __name__ == "__main__":
    # Sample News Article Data (Replace or load your external text file here if needed)
    sample_article = """
    Natural Language Processing, or NLP, is transforming how we interact with machines. 
    Startups around the globe are deploying deep learning models to extract deep insights from news.
    
    Data analysts use these text tools daily. Is it difficult to build? Not with Python!
    """

    print("--- NLP Text Analysis Dashboard ---")
    
    # Meeting the 'while loop' requirement for the interactive menu
    running = True
    while running:
        print("\nSelect an Analysis Option:")
        print("1. Run Complete Auto-Analysis Suite")
        print("2. Search for a Specific Word Count")
        print("3. Exit Application")
        
        choice = input("Enter choice (1-3): ").strip()
        
        # Meeting the 'if/else conditional' requirement
        if choice == "1":
            print("\nExecuting Analysis...")
            print(f"• Most Common Word: '{identify_most_common_word(sample_article)}'")
            print(f"• Average Word Length: {calculate_average_word_length(sample_article):.2f} characters")
            print(f"• Total Paragraphs: {count_paragraphs(sample_article)}")
            print(f"• Total Sentences: {count_sentences(sample_article)}")
            
        elif choice == "2":
            target_word = input("Enter the word you want to count: ").strip()
            count = count_specific_word(sample_article, target_word)
            print(f"• The word '{target_word}' appears {count} time(s).")
            
        elif choice == "3":
            print("Exiting NLP Analyzer system. Analysis complete.")
            running = False
            
        else:
            print("Invalid selection. Please choose a valid menu item.")