# The Literary Time Machine 📚⏳

### Quantifying the Evolution of Literature using NLP & Python

**Project Status:** ✅ Complete

## 📖 Overview
Does human emotion change over centuries? Do we use simpler words today than we did in the 1800s?

**The Literary Time Machine** is a Data Science pipeline that ingests, cleans, and analyzes full-text novels from Project Gutenberg to answer these questions. By processing over **500,000+ words** of unstructured text data, this project quantifies the "shape" of stories and tracks cultural shifts in vocabulary (e.g., the rise of "Technology" vs. the fall of "Tradition").

## 📊 Key Features
* **Automated ETL Pipeline:** Scrapes raw text from Project Gutenberg, removes licensing headers, and normalizes text for analysis.
* **Sentiment Analysis (VADER):** Maps the emotional arc of novels (Tragedy vs. Happy Endings) using a rolling-average sentiment score.
* **Lexical Diversity Scoring:** Calculates the vocabulary richness of authors to test the "Dumbing Down" hypothesis.
* **Interactive Visualization:** A Plotly dashboard mapping 200+ years of literature by sentiment and complexity.

## 🛠️ Tech Stack
* **Language:** Python 3.12
* **Data Manipulation:** Pandas, NumPy
* **Natural Language Processing:** NLTK (Tokenization, Stopword Removal, VADER Sentiment)
* **Visualization:** Plotly (Interactive), Matplotlib/Seaborn (Static)
* **Version Control:** Git & GitHub

## 📈 Visual Insights

### 1. The Emotional Arc of a Story
*Mapping the rise and fall of happiness in "Pride and Prejudice" vs. "Frankenstein".*
![Emotional Arc](figures/sentiment_arc.png)

### 2. The Literary Map (Interactive)
*Clustering books by emotional tone and vocabulary complexity.*
![Interactive Plot](figures/literary_map.png)

## 💡 Key Findings
1.  **The Gothic Paradox:** Despite being written in the late 19th century, *Dracula* scores lower on "Modernity" keywords than books from 1813, proving that **Genre** is a stronger predictor of vocabulary than **Time**.
2.  **The Happiness Singularity:** Initial analysis using VADER on full texts resulted in saturation (Score = 1.0). The pipeline was optimized to score sentence-chunks and average them for a realistic emotional distribution.

## 🚀 How to Run
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/literary-time-machine.git](https://github.com/yourusername/literary-time-machine.git)
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the analysis pipeline:**
    ```bash
    python scripts/6_interactive_viz.py
    ```

## 👤 Author
**Bea Andrea Gamilong**
*Computer Science Student specializing in Data Science | University of Santo Tomas*
[LinkedIn](https://www.linkedin.com/in/bea-andrea-gamilong) | [Email](mailto:beaandreagamilong@gmail.com)