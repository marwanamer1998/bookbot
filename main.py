from stats import count_words, count_chars, sorted_list
import sys

if len(sys.argv) != 2:
   print("Usage: python3 main.py <path_to_book>")
   sys.exit(1)


   
def main():
    with open(sys.argv[1]) as f:
        file_content = f.read()
    return file_content

file_content = main()

print("===========BOOKBOT===========")
print(f"Analyzing book found at {sys.argv[1]}")
print("----------- Word Count -----------")
word_count = count_words(file_content)
print(f"Found {word_count} total words")
print("--------- Character Count --------")

char_count = count_chars(file_content)
char_list_sorted = sorted_list(char_count)

for item in char_list_sorted:
    if item["char"].isalpha():
        print(f"{item['char']}: {item['num']}")

print("============= END ===============")

print(sys.argv)