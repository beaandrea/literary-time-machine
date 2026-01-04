import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

INPUT_FILE = "data/processed/corpus.csv"

def calculate_diversity(text):
    """
    Lexical Diversity = (Unique Words) / (Total Words)
    A higher number means the author uses a wider vocabulary range.
    """
    if not isinstance(text, str): return 0
    words = text.split()
    if len(words) == 0: return 0
    unique_words = set(words)
    diversity = len(unique_words) / len(words)
    return diversity

def get_top_words(text, n=10):
    # Returns the top N most frequent words in a text string.
    if not isinstance(text, str): return []
    words = text.split()
    counter = Counter(words)
    return counter.most_common(n)

def main():
    print("--- Loading Data ---")
    df = pd.read_csv(INPUT_FILE)

    # 1. Calculate Lexical Diversity
    df['lexical_diversity'] = df['clean_text'].apply(calculate_diversity)

    # 2. Print "Report Card"
    print("\n--- Literary Report Card ---")
    print(f"{'Title':<30} | {'Year':<6} | {'Diversity Score'}")
    print("-" * 60)
          
    for index, row in df.iterrows():
          print(f"{row['title'][:30]:<30} | {row['year']:<6} | {row['lexical_diversity']:.2%}")

    # 3. Quick Visualization of Diversity
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='year', y='lexical_diversity', hue='title', palette='viridis')
    plt.title("Lexical Diversity: Did Vocabulary shrink Over Time?")
    plt.ylabel("Unique Words / Total Words")
    plt.tight_layout()
    plt.show()

    # Check Top Words
    print("\n---TOP 5 WORDS PER BOOK---")
    for index, row in df.iterrows():
        top_words = get_top_words(row['clean_text'], n=5)
        print(f"{row['title']}: {top_words}")

if __name__ == "__main__":
    main()