from Node import Node, SingleLinkedList, Queue, BST


test_data = [1,3,4,5,6,8,7,9,2,22,15,55,45,23,24,26,28]

LLI = SingleLinkedList()

queue = Queue()

root = BST(None)
for item in test_data:
    LLI.add_end(item)#Testing to add data from the beginning
# LLI.add_between_after(40, 22)
# LLI.add_between_before(23, 55)
# LLI.delete_end()
# LLI.delete_by_value(9)
# LLI.minimum_number()
# LLI.print_linked_list()

for item in test_data:
    queue.enqueue(item)
queue.sort_queue()
queue.display()




# for item in test_data:
#      root.insert(item)

