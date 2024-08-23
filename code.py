import tkinter as tk
from tkinter import filedialog
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import docx

def load_file(file_path):
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    elif file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        return '\n'.join([p.text for p in doc.paragraphs])
    else:
        raise ValueError("Unsupported file format")

def calculate_similarity(text1, text2):
    # Create TF-IDF vectors for both texts
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    
    # Calculate cosine similarity between the two vectors
    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity_matrix[0][0]

def select_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("Word Documents", "*.docx"), ("All Files", "*.*")],
        title="Select a file"
    )
    return file_path

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    print("Select the first file:")
    file1 = select_file()
    print("Select the second file:")
    file2 = select_file()

    try:
        # Load the text from the files
        text1 = load_file(file1)
        text2 = load_file(file2)

        # Calculate similarity
        similarity_score = calculate_similarity(text1, text2)
        
        print(f"Similarity Score: {similarity_score:.4f}")
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
