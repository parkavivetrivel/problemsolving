def count_substring(string, sub_string):
    occurnace = []
    length_substring = len(sub_string)
    for i in range(0, len(string)):
        if string[i:length_substring] == sub_string:
            occurnace.append(sub_string)
        length_substring += 1
    return len(occurnace)



print(count_substring("ABCDCDC","CDC"))