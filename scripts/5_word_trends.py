import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from collections import Counter

# The input dataset
INPUT_FILE = "data/processed/corpus.csv"

# Themes I wanna track
TARGET_KEYWORDS = {
    "Tradition": ["honor", "duty", "soul", "god", "pray"],
    "Modernity": ["money", "business", "train", "car", "city"],
    "Emotion": ["love", "heart", "feel", "happy", "sad"],
    "Society": ["class", "rich", "poor", "status", "power"]
}

def count_concept_mentions(text, concept_words):
    """Counts how many times any word from the concept list appears in the text."""
    if not isinstance(text, str): return 0
    words = text.split()

    # Create a frequency dictionary for the text
    word_counts = Counter(words)

    total = 0
    for concept in concept_words:
        # Get the count for the specific word
        total += word_counts[concept]
    
    return total

def main():
    print(f"--- Starting Keyword Trend Analysis ---")

    # 1. Load the data
    df = pd.read_csv(INPUT_FILE)

    # 2. Analyze each theme
    # I will create new columns for each theme
    for theme_name, word_list in TARGET_KEYWORDS.items():
        print(f"Analyzing theme: {theme_name} {word_list}...")

        # Calculate raw counts
        col_name_raw = f"{theme_name}_raw"
        df[col_name_raw] = df['clean_text'].apply(lambda x: count_concept_mentions(x, word_list))

        # Normalization
        col_name_norm = f"{theme_name}_freq"
        df[col_name_norm] = (df[col_name_raw] / df['clean_word_count']) * 10000
    
    # Visualization
    plt.figure(figsize=(12, 6))

    # Plot a line for each theme
    for theme_name in TARGET_KEYWORDS.keys():
        # Sort by year first to make the line connect properly
        df_sorted = df.sort_values(by="year")

        plt.plot(df_sorted['year'], df_sorted[f"{theme_name}_freq"], marker='o', linewidth=2, label=theme_name)

        # Label the points with book titles
        for i, txt in enumerate(df_sorted['title']):
            # Only label if it's a "peak" to avoid clutter
            if i % 1 == 0:
                plt.annotate(txt[:10], # First 10 chars of title
                             (df_sorted['year'].iloc[i], df_sorted[f"{theme_name}_freq"].iloc[i]),
                             xytext=(5,5), textcoords='offset points', fontsize=8)
    
    plt.title("The Shift in Values: Tracking Themes Across Centuries")
    plt.xlabel("Year Published")
    plt.ylabel("Mentions per 10,000 Words")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    print("--- Plotting Trends ---")
    plt.show()

    # 4. Save the enriched data
    df.to_csv("data/processed/corpus_with_themes.csv", index=False)
    print("Saved enriched dataset to data/processed/corpus_with_themes.csv")

if __name__ == "__main__":
    main()