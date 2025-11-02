def get_num_words(text):
	return len(text.split())

def get_num_chars(text):
	chars = {}
	for ch in text:
		ch = ch.lower()
		if ch in chars:
			chars[ch] += 1
		else:
			chars[ch] = 1
	return chars

def sort_on(chars):
	return chars["num"]

def sort_text(char_counts):
	result = []
	for ch, num in char_counts.items():
		new_dict = {"char": ch, "num": num}
		result.append(new_dict)
	result.sort(reverse=True, key=sort_on)
	return result
