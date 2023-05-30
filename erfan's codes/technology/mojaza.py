
def separator(ls):
    even_list = []
    odd_list = []
    for number in ls:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)
    return (even_list, odd_list)
