

from doubly_linked_list import DoublyLinkedList

input = '1950139 0 3 837 6116 18472 228700 45'
# input = '125 17'
blinks = 25


dll = DoublyLinkedList()

for number in input.split():
    dll.append(int(number))

dll.display()


while blinks:
    current = dll.head

    while current:
        if current.value == 0:
            current.value = 1
            current = current.next
            continue
        if len(str(current.value)) % 2 == 0:
            next = current.next
            left, right = int(str(current.value)[:len(str(current.value))//2]), int(str(current.value)[len(str(current.value))//2:])
            current.value = left
            dll.insert(current, right)
            current = next
            continue
        current.value *= 2024
        current = current.next
    print(blinks, dll.length)
    blinks -= 1

print(dll.length)