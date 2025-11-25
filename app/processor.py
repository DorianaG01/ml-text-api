import re

class TextProcessor:
    
    # Internal library handling only business logic and transformations.

    def __init__(self, remove_digits: bool = False):
        self.remove_digits = remove_digits  # Option to remove numbers from text

    def clean_text(self, text: str) -> str:
        
        # Cleans text by removing special characters and extra spaces
        # Uses standard regular expressions to identify specific patterns
        
        if not text:
            return ""

        # 1. Convert to lowercase
        cleaned = text.lower()

        # 2. Remove numbers 
        if self.remove_digits:
            cleaned = re.sub(r'\d+', '', cleaned)

        # 3. Remove punctuation 
        cleaned = re.sub(r'[^\w\s]', '', cleaned)

        # 4. Remove extra spaces
        cleaned = " ".join(cleaned.split())

        return cleaned

    def analyze_stats(self, text: str) -> dict:
        # Returns statistics about the text.
        words = text.split()
        return {
            "word_count": len(words), 
            "char_count": len(text),
            "original_length": len(text)
        }
