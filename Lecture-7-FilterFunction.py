nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)


# odd 1,3,5,7,9
# even 2,4,6,8,10

def is_odd(num):
    for x in range(2, num):
        if (num % 2) == 0:  # the number is even!
            return False
        return True



odds = list(filter(is_odd, nums))
print(odds)
