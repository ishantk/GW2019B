def showList(numbers):
    print("HashCode of numbers:", hex(id(numbers)))
    size = len(numbers) # 5
    for i in range(0, size): # from 0 to < size
        numbers[i] = numbers[i] * numbers[i]

    print("numbers is:",numbers) # [1, 4, 9, 16, 25]



data = [1, 2, 3, 4, 5]
print("HashCode of data:",hex(id(data)))
showList(data)
print("data is:",data)           # [1, 2, 3, 4, 5]
