# print a triangle made of stars, with a base of 5
def count_up(start, end):
    if start <= end:
        print(start)
        count_up(start + 1, end)
    return


count_up(0, 10)
