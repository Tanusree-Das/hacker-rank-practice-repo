'''A newly opened multinational brand has decided to base their company logo on the three most common characters in the
company name. They are now trying out various combinations of company names and logos based on this condition. Given a string ,
 which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.'''

from collections import Counter

def get_key_from_value(d, val):
    keys = [k for k, v in d.items() if v == val]
    keys.sort()
    return keys

def solution_by_tannu(s):
    final_dict = dict()
    list_to_work_with = list()
    x = Counter([*s])
    full_dict = dict(x)
    top3 = x.most_common(3)
    top3_dict = dict(top3)
    counter = 0

    for i in top3_dict.values():  # sort by alphabet
        list_to_work_with.append(get_key_from_value(full_dict, i))
        for j in list_to_work_with[0]:
            final_dict[j] = i
        list_to_work_with = []
    for i, j in final_dict.items():
        if counter < 3:
            print(i, j)
            counter = counter + 1

def solution_by_chatgpt(s):
    char_count=Counter(s)
    sorted_char_count=sorted(char_count.items(), key=lambda x:(-x[1],x[0])) #need to read this part
    for i in sorted_char_count[:3]:
        print(*i)



if __name__ == '__main__':
    s = input()
    print("solution by tannu")
    solution_by_tannu(s)
    print("solution by chatgpt")
    solution_by_chatgpt(s)




