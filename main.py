from LinkedList.linkedlist import SingleLinkedList
from LinkedList.doublelinkedlist import DoubleLinkedList

obj_list = SingleLinkedList()
obj_list.create_list()

obj_list2 = DoubleLinkedList()
obj_list2.create_list()


def single_linked_list_practice():
	while True:
		print("1. Display list")
		print("2. Count the number of nodes")
		print("3. Search for an element")
		print("4. Insert in beginning of the list")
		print("5. Insert a node at the end of the list")
		print("6. Insert a node after a specified node")
		print("7. Insert a node before a specified node")
		print("8. Insert a node at a given position")
		print("9. Delete first node")
		print("10. Delete last node")
		print("11. Delete any node")
		print("12. Reverse the list")
		print("13. Bubble sort by exchanging data")
		print("14. Bubble sort by exchanging links")
		print("15. MergeSort")
		print("16. Insert Cycle")
		print("17. Detect Cycle")
		print("18. Remove Cycle")
		print("19. Quit")

		option = int(input("Enter your choice: "))

		if option == 1:
			obj_list.display_list()
		elif option == 2:
			obj_list.count_node()
		elif option == 3:
			data = int(input("Enter the element to be searched: "))
			obj_list.search(data)
		elif option == 4:
			data = int(input("Enter the element to be inserted: "))
			obj_list.insert_in_beginning(data)
		elif option == 5:
			data = int(input("Enter the element to be inserted: "))
			obj_list.insert_at_end(data)
		elif option == 6:
			data = int(input("Enter the element to be inserted: "))
			x = int(input("Enter the element after which to insert: "))
			obj_list.insert_after(data, x)
		elif option == 7:
			data = int(input("Enter the element to be inserted: "))
			x = int(input("Enter the element before which to insert: "))
			obj_list.insert_before(data, x)
		elif option == 8:
			data = int(input("Enter the element to be inserted: "))
			k = int(input("Enter the position at which to insert: "))
			obj_list.insert_at_position(data, k)
		elif option == 9:
			obj_list.delete_fisrt_node()
		elif option == 10:
			obj_list.delete_last_node()
		elif option == 11:
			data = int(input("Enter the element to be deleted: "))
			obj_list.delete_node(data)
		elif option == 12:
			obj_list.reverse_list()
		elif option == 13:
			obj_list.bubble_sort_exdata()
		elif option == 14:
			obj_list.buble_sort_exlink()
		elif option == 15:
			obj_list.merge_sort()
		elif option == 16:
			data = int(input("Enter the element at which the cycle has to be inserted: "))
			obj_list.insert_cycle(data)
		elif option == 17:
			if obj_list.has_cycle():
				print("List has a cycle.")
			else:
				print("List doesn't have a cycle.")
		elif option == 18:
			obj_list.remove_cycle()
		elif option == 19:
			break
		else:
			print("Wrong option")
		print()


def double_linked_list():
	while True:
		print("1. Display list")
		print("2. Insert in empty list")
		print("3. Insert a node in the beginning of the list")
		print("4. Insert a node at the end of the list")
		print("5. Insert a node after a specified node")
		print("6. Insert a node before a specified node")
		print("7. Delete first node")
		print("8. Delete last node")
		print("9. Delete any node")
		print("10. Reverse the list")
		print("11. Quit")

		option = int(input("Enter your choice: "))

		if option == 1:
			obj_list2.display_list()
		elif option ==2:
			data = int(input("Enter element to be inserted: "))
			obj_list2.insert_in_empty_list(data)
		elif option == 3:
			data = int(input("Enter element to be inserted: "))
			obj_list2.insert_in_begining(data)
		elif option == 4:
			data = int(input("Enter element to add: "))
			obj_list2.insert_at_end(data)
		elif option == 5:
			data = int(input("Enter element to add: "))
			x = int(input("Enter position: "))
			obj_list2.insert_after(data, x)
		elif option == 6:
			data = int(input("Enter element to add: "))
			x = int(input("Enter position: "))
			obj_list2.insert_before(data, x)
		elif option == 7:
			obj_list2.delete_first_node()
		elif option == 8:
			obj_list2.delete_last_node()
		elif option == 9:
			x = int(input("Choose element to delete: "))
			obj_list2.delete_node(x)
		elif option == 10:
			obj_list2.reverse_list()
		elif option == 11:
			break
		else:
			print("Wrong option")
		print()


# single_linked_list_practice()
double_linked_list()

