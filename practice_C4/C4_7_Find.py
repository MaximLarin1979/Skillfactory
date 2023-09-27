def count(array, element):
    a = 0
    for i in array:
        if i == element:
            a += 1
    return a

array = list(map(int, input().split()))
print(array)
element = int(input())

print(count(array, element))