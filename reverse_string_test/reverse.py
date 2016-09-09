def reverse_string(str):
    result = ""
    for i in xrange(len(str)-1, -1, -1):
        result += str[i]

    return result
