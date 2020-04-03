evenList [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_even(num):
    for num in evenList:
        if(evenList[num] % 2 == 0):
            print("True")
        else:
            print("False")

is_even(3)
is_even(8)
