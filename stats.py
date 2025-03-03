def get_word_count(text):
    #num_words = 0
    line = text.split()
    #num_words += len(line)

    #return num_words
    return len(line)
    
def get_char_count(text):
    letters_dict = {}

    for letter in text:
        lowercase_letter = letter.lower()

        if lowercase_letter in letters_dict:
            letters_dict[lowercase_letter] += 1
        else:
            letters_dict[lowercase_letter] = 1
    
    return letters_dict

def get_alpha_chars(dict):
    alpha_char = []
    for key, value in dict.items():
        if key.isalpha():
            character = []
            character.append(key)
            character.append(value)
            
            alpha_char.append(character)

    return alpha_char

def get_sorted_char(dict):
    list = get_alpha_chars(dict)
    list.sort(reverse=True, key=sort_on)

    return list

def sort_on(list):
    return list[1]

'''
def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
'''