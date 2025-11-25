chars={}

def get_value(dict):
    values = dict["num"]
    return values

def count_chars(text):
    text=text.lower()
    for char in text:
        if char in chars:
            chars[char]+=1
        else:
            chars[char]=1
    return chars


def count_words(text):
    words=[]
    words=text.split()
    return len(words)

def sort_dict(words_dict):
    sorted_list=[]
    for char in words_dict:
        if char.isalpha():
            new_dict= {"char":char,  "num":words_dict[char]}
            sorted_list.append(new_dict)
    sorted_list=sorted_list    
    sorted_list.sort(key=get_value, reverse=True)
    return sorted_list