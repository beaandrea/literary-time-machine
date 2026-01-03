import os
import string
import pandas as pd
import nltk
from nltk.corpus import stopwords

RAW_DATA_FOLDER = "data"
PROCESSED_FOLDER = "data/processed"

def setup_folder():
    """Create the data folder if it doesn't exist."""
    if not os.path.exists(PROCESSED_FOLDER):
        os.makedirs(PROCESSED_FOLDER)
        print(f"Created folder: {PROCESSED_FOLDER}")

def clean_text(text):
    # First: Lowercase
    text.lower()

    # Tokenize (split string into list of words)
    tokens = nltk.word_tokenize(text)

    # Remove punctuations
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]

    # Remove non-alphabetic tokens
    words = [word for word in stripped if word.isalpha()]

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]

    return words

def main():
    setup_folder()

    # Store the data in a list of dictionaries to convert to a DataFrame
    corpus_data = []

    print("--- Starting Text Cleaning ---   ")

    # Loop through all files in the data folder
    for filename in os.listdir(RAW_DATA_FOLDER):
        if filename.endswith(".txt"):
            file_path = os.path.join(RAW_DATA_FOLDER, filename)

            print(f"Preprocessing: {filename}...")

            # Read the raw file
            with open(file_path, "r", encoding="utf-8") as f:
                raw_text = f.read()

            # Clean the text
            clean_tokens = clean_text(raw_text)

            # Extract metadata from filename (assuming that the format is YEAR_TITLE.txt)
            year = filename.split("_")[0]
            title = filename.replace(".txt", "")

            # Add to list
            corpus_data.append({
                "filename": filename,
                "year": int(year),
                "title": title,
                "raw_text_length": len(raw_text),
                "clean_word_count": len(clean_tokens),
                "clean_text": " ".join(clean_tokens) # join tokens back into a string for easy CSV saving
            })
        
        # Convert to DataFrame
        df = pd.DataFrame(corpus_data)

        # Sort by year
        df = df.sort_values(by="year")

        # Save to CSV
        output_path = os.path.join(PROCESSED_FOLDER, "corpus.csv")
        df.to_csv(output_path, index=False)

        print(f"\n--- Success! ---")
        print(f"Processed {len(df)} books.")
        print(f"Saved cleaned data to {output_path}")
        print(f"\n Preview of the data:")
        print(df[["year", "title", "clean_word_count"]].head())

if __name__ == "__main__":
    main()

    