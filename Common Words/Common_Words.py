from pathlib import Path

def common_word(filename, target):
    """Returns the amount of how many times a word appears in a text"""
    path = Path(filename)
    words = path.read_text(encoding='utf-8')
    count = words.lower().count(target.lower())
    return count

print(common_word('hungarian literature.txt', 'hungarian'))

