def fizzbuzz(num):
    # if num == 3:
    #     return "fizz"
    #
    # if num == 5:
    #     return "buzz"
    #
    # if num == 15:
    #     return "fizzbuzz"
    #
    # if num == 4:
    #     return 4

    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"

    elif num % 3 == 0:
        return "fizz"

    elif num % 5 == 0:
        return "buzz"

    else:
        return num


# fizzbuzz(10)
