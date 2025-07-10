def count_words(file_content):
   return len(file_content.split())


def count_chars(file_content):
   char_dict = {}
   for char in file_content:
      lower_char = char.lower()
      if lower_char not in char_dict:
         char_dict[lower_char] = 1
      else:
         char_dict[lower_char] += 1
   return char_dict

def sort_on(dict_item):
    return dict_item["num"]

def sorted_list(char_dict):
    result = []
    for k, v in char_dict.items():
        result.append({"char": k, "num": v})
    result.sort(reverse=True, key=sort_on)
    return result

      

   