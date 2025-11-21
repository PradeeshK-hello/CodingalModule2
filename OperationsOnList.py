list = ["Apple", "Guava", "Mango", "Banana", "Kiwi"]

print("Length of list:", len(list))
print("First Element:", list[0])
print("Last Element:", list[-1])

list.append("Papaya")
print("Updated List:", list)

list.remove("Guava")
print("Updated List:", list)

list.sort()
print("Sorted List:", list)

list.pop(1)
print("Updated List:", list)

list.reverse()
print("Reversed List:", list)

print("Multiplication on List:", list*2)

list = list[:4]
print("Sliced List:", list)

list.clear()
print("Updated List:", list)