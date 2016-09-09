def word_summary(str):
    if str == "":
        return {}
    str = str.split(" ")
    word_count = {};
    for word in str:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    return word_count
