def main():
    book_name = "books/frankenstein.txt"
    with open(book_name) as f:
        print(f"--- Begin report of {book_name} ---")
        file_contents = f.read()
        wc = word_count(file_contents)
        print(f"{wc} words found in the document")
        print(f"")
        letters = return_list_of_dicts(letter_counts(file_contents))
        for dict in letters:
            if not dict["name"].isalpha():
                continue
            print(f"The '{dict['name']}' character was found {dict['num']} times")

def word_count(s):
    return len(s.split())

def letter_counts(s):
    letters = {}
    for c in s.lower():
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1
    return letters

def sort_on(dict):
    return dict["num"]

def return_list_of_dicts(dict):
    list_of_dicts = []
    for key in dict:
        if not key.isalpha():
            continue
        new_dict = {}
        new_dict["name"] = key
        new_dict["num"] = dict[key]
        list_of_dicts.append(new_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

main()
