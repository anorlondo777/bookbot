from stats import get_num_chars, get_num_words, sort_text
import sys

def get_book_text(filepath):
        with open(filepath) as f:
                contents = f.read()
        return contents

def main(path):
	text = get_book_text(path)
	total_words = get_num_words(text)
	dictionary = get_num_chars(text)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	print("----------- Word Count ----------")
	print(f"Found {total_words} total words")
	print("--------- Character Count -------")
	sorted_list = sort_text(dictionary)
	for item in sorted_list:
		if not item["char"].isalpha():
			continue
		print(f"{item['char']}: {item['num']}")
	print("============= END ===============")

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

path = sys.argv[1]
main(path)
