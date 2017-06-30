def add_two_numbers(arg1, arg2):
    sum = int(arg1) + int(arg2)
    return sum


def test_add_two_numbers(add):
    sum = add_two_numbers(add['arg1'], add['arg2'])
    # string = str(add['arg1']) + '+' + str(add['arg2']) + '=' + str(sum)
    # print(string)
    print("{} + {} = {}".format(add['arg1'], add['arg2'], sum))
    assert sum == add['expected']
