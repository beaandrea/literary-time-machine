import pandas as pd
import plotly.express as px
import os

INPUT_FILE = "data/processed/corpus.csv"
OUTPUT_HTML = "interactive_literary_map.html"

# Gonna have to re-run the computations since I didn't save these to CSV in the previous steps

from nltk.sentiment.vader import SentimentIntensityAnalyzer

def calculate_metrics(df):
    print("Recalculating metrics for visualization...")

    # 1. Diversity (Simple vs complex)
    df['lexical_diversity'] = df['clean_text'].apply(
        lambda x: len(set(x.split())) / len(x.split()) if isinstance(x, str) else 0
    )

    # 2. Sentiment (Tragedy vs Comedy)
    sia = SentimentIntensityAnalyzer()
    df['sentiment'] = df['clean_text'].apply(
        lambda x: sia.polarity_scores(x[:5000])['compound'] if isinstance(x, str) else 0
    )

    return df

def main():
    print("--- Loading Data ---")
    df = pd.read_csv(INPUT_FILE)

    df = calculate_metrics(df)

    print("--- Building Interactive Chart ---")

    fig = px.scatter(
        df,
        x = "sentiment",
        y = "lexical_diversity",
        color = "year",
        size = "clean_word_count",
        hover_name = "title",
        hover_data = ["year", "clean_word_count"],
        title = "The Literary Map: Sentiment vs Vocabulary Complexity",
        labels = {
            "sentiment": "Emotional Tone (-1 = Tragic, +1 = Happy)",
            "lexical_diversity": "Vocabulary Richness (Higher = More Unique Words)",
            "year": "Publication Year"
        },
        template = "plotly_white"
    )

    # Add Neutral Sentiment (line)
    fig.add_vline(x=0, line_width=1, line_dash="dash", line_color="white")

    # Save as an HTML file
    print(f"Saving to {OUTPUT_HTML}...")
    fig.write_html(OUTPUT_HTML)

    print("Done! Go open the HTML file in your folder.")

    try:
        os.startfile(OUTPUT_HTML)
    except:
        pass

if __name__ == "__main__":
    main()


