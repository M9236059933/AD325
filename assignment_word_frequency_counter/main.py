import re

def count_word_frequency(text):
    # Normalize text: lowercase and remove punctuation (except spaces)
    text = text.lower()
    text = re.sub(r'[^a-z0-9 ]', '', text)

    # Split text into words by whitespace
    words = text.split()

    # Create a dictionary
    freq_map = {}

    # Count frequency of each word
    for word in words:
        freq_map[word] = freq_map.get(word, 0) + 1

    return freq_map

def main():
    # Prompt user for input
    text = input("Paste your text and press Enter:\n\n")

    # Count frequencies
    frequencies = count_word_frequency(text)

    # Sort the result by keys (alphabetically)
    print("\nWord Frequencies:\n")
    for word in sorted(frequencies):
        print(f"{word}: {frequencies[word]}")

if __name__ == "__main__":
    main()