largest = None
smallest = None
lst = []
n = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        lst.append(int(num))
        largest = lst[0]
        smallest = lst[0]
        for i in lst:
            if i > largest:
                largest = i
        for i in lst:
            if i < smallest:
                smallest = i
    except:
        print("Invalid input")


print("Maximum", largest)
print("Minimum", smallest)