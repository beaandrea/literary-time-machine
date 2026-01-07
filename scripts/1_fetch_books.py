import requests
import os
import time

# Folder where books will be saved
DATA_FOLDER = "data"

# Dictionary of book IDs and their filenames (popular books from three distinct eras)
BOOKS = {
    # Era 1: The Romantics (1810 - 1850)
    1342: "1813_pride_and_prejudice",
    84: "1818_frankenstein",

    # Era 2: The Victorians (1850 - 1890)
    98: "1859_tale_of_two_cities",
    76: "1884_huckleberry_finn",

    # Era 3: The Modernists (1890 - 1925)
    345: "1897_dracula",
    64317: "1925_great_gatsby"
}

def setup_folder():
    """Create the data folder if it doesn't exist."""
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)
        print(f"Created folder: {DATA_FOLDER}")

def download_book(book_id, filename):
    """Downloads book text from Project Gutenberg"""
    url = f"https://www.gutenberg.org/cache/epub/{book_id}/pg{book_id}.txt"
    save_path = os.path.join(DATA_FOLDER, f"{filename}.txt")

    print(f"Downloading: {filename} (ID: {book_id})...")

    try:
        response = requests.get(url)
        response.raise_for_status() # Check for errors

        text = response.text

        # Since Project Gutenberg has legal headers and footers, we'd want to remove them.
        start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK ***"
        end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK ***"

        start_index = text.find(start_marker)
        end_index = text.find(end_marker)

        # If markers are found, slice the text to keep only the middle story
        if start_index != -1 and end_index != -1:
            # Move index forward to skip the marker line itself (~100 chars buffer)
            content_start = text.find("\n", start_index) + 1
            text = text[content_start:end_index]
            print(f"Successfully stripped headers.")
        else:
            print(f"Warning: Markers not found. Saving raw text.")
        
        # Save to file
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(text)
        
        print(f"Saved to {save_path}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

def main():
    setup_folder()
    print("--- Starting Bulk Download ---")
    
    for book_id, filename in BOOKS.items():
        download_book(book_id, filename)
        time.sleep(3) # To avoid overwhelming the server

    print("--- Download complete! ---")

if __name__ == "__main__":
    main()