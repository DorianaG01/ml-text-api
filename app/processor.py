import re

class TextProcessor:
    
    #Libreria interna che si occupa solo della business logic e delle trasformazioni.
    

    def __init__(self, remove_digits: bool = False):
        self.remove_digits = remove_digits  # Opzione per rimuovere i numeri dal testo

    def clean_text(self, text: str) -> str:
     
        #Pulisce il testo rimuovendo caratteri speciali e spazi extra
        #Usa regular expressions standard per identificare pattern specifici
        
        if not text:
            return ""

        # 1. Converti a minuscolo
        cleaned = text.lower()

        # 2. Rimuovi numeri 
        if self.remove_digits:
            cleaned = re.sub(r'\d+', '', cleaned)

        # 3. Rimuovi punteggiatura 
        cleaned = re.sub(r'[^\w\s]', '', cleaned)

        # 4. Rimuovi spazi extra
        cleaned = " ".join(cleaned.split())

        return cleaned

    def analyze_stats(self, text: str) -> dict:
        #Restituisce statistiche sul testo.
        words = text.split()
        return {
            "word_count": len(words), 
            "char_count": len(text),
            "original_length": len(text)
        }