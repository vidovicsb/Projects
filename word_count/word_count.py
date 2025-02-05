from pathlib import Path

def word_count(path):
    """Counts the amount of words in a .txt file"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"The file {path} is not found.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The book {str(path).removesuffix('.txt')} has approximately {num_words} words in it.")
        
books = ['The Flying Carpet', 'The Doctor Looks at Literature', 'Light Interviews With Shades', 'Hungarian Literature']

for book in books:
    path = Path(book+".txt")
    word_count(path)