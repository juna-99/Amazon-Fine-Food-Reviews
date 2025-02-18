import re
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Compile regex patterns
HTMLTAGS = re.compile(r'<.*?>')  # Remove HTML tags
MULTIPLE_WHITESPACE = re.compile(r'\s{2,}')  # Replace multiple spaces with single space

# Define translation tables
table = str.maketrans("", "", string.punctuation)  # Remove punctuation
remove_digits = str.maketrans("", "", string.digits)  # Remove digits

# Load stopwords
final_stopwords = set(stopwords.words('english'))

# Initialize stemmer
stemmer = PorterStemmer()

def preprocessor(review):
    """Cleans and preprocesses a review: removes HTML, punctuation, digits, stopwords, and applies stemming."""
    # Remove HTML tags
    review = HTMLTAGS.sub(r'', review)

    # Remove punctuation
    review = review.translate(table)

    # Remove digits
    review = review.translate(remove_digits)

    # Convert to lowercase
    review = review.lower()

    # Replace multiple white spaces with a single space
    review = MULTIPLE_WHITESPACE.sub(" ", review).strip()

    # Remove stopwords
    review = [word for word in review.split() if word not in final_stopwords]

    # Apply stemming
    review = ' '.join([stemmer.stem(word) for word in review])

    return review
