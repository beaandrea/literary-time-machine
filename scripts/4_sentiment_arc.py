import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

RAW_DATA_FOLDER = "data"

def get_sentiment_arc(text, window_size=500):
    """Breaks text into sentences, scores them, and calculates a rolling average 
    to show the 'shape' of the story."""

    # Initialize the AI scorer
    sia = SentimentIntensityAnalyzer()

    # 1. Break into sentences
    sentences = nltk.tokenize.sent_tokenize(text)

    # 2. Score each sentence
    scores = [sia.polarity_scores(s)['compound'] for s in sentences]

    # 3. Create a Pandas Series to smooth the data
    series = pd.Series(scores)
    smoothed_scores = series.rolling(window=window_size).mean()

    return smoothed_scores

def main():
    print("--- Starting Sentiment Analysis ---")

    plt.figure(figsize=(12, 6))

    # Loop through files
    for filename in os.listdir(RAW_DATA_FOLDER):
        if filename.endswith(".txt"):
            print(f"Analyzing: {filename}...")

            # Read raw text
            file_path = os.path.join(RAW_DATA_FOLDER, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

            # Get the arc
            arc = get_sentiment_arc(text)

            # Plot using distinct colors for clarity
            label = filename.replace(".txt", "")
            plt.plot(arc, label=label, linewidth=2)
    
    # More chart customization
    plt.title("The Emotional Arc of Literature (Rolling Average)", fontsize=16)
    plt.xlabel("Narrative Time (Sentence Index)", fontsize=12)
    plt.ylabel("Sentiment (Negative < 0 < Positive)", fontsize=12)
    plt.axhline(0, color='black', linewidth=1, linestyle='--') # This is the nautral line
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left') # Put legend outside plot
    plt.grid(alpha=0.3)
    plt.tight_layout()

    print("--- Plotting Results ---")
    plt.show()

if __name__ == "__main__":
    main()
