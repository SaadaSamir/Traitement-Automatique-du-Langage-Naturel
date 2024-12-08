import spacy
from collections import Counter
import string

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Function for text preprocessing
def preprocess_text(text, frequent_word_threshold=5, rare_word_threshold=1):
    #Lower casing
    text = text.lower()
    
    # Process the text using spaCy
    doc = nlp(text)
    
    # Step 2: Tokenization, Lemmatization, and Removal of Punctuations and Stopwords
    lemmatized_tokens = [token.lemma_ for token in doc 
                         if token.text not in string.punctuation and
                         not token.is_stop and token.lemma_ != "-PRON-"]
    
    # Step 3: Calculate word frequency (after lemmatization)
    word_freq = Counter(lemmatized_tokens)
    
    # Step 4: Remove frequent and rare words based on thresholds
    processed_tokens = [token for token in lemmatized_tokens 
                        if word_freq[token] < frequent_word_threshold and
                        word_freq[token] > rare_word_threshold]
    
    # Join the processed tokens back into a single string
    processed_text = " ".join(processed_tokens)
    
    return processed_text

text = """
Spacy is an excellent library for natural language processing. 
It has various tools like tokenization, lemmatization, and POS tagging, 
making it very useful for text preprocessing tasks.
"""

preprocessed_text = preprocess_text(text)


print(preprocessed_text)
