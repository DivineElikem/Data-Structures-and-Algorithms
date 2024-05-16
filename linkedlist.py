class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


def traverse(head: Node):
    current_node = head
    while current_node:
        print(current_node.value, end="->")
        current_node = current_node.next
    print("null")


def is_in_list(head: Node, search_node: Node):
    current_node = head
    while current_node:
        if search_node == current_node:
            return True
        current_node = current_node.next
    return False

def search(head: Node, search_node: Node):
    in_list = is_in_list(head, search_node)
    if in_list:
        print(f"Node with value {search_node.value} exists in the linked list")
    else:
        print(f"Sorry, node with value {search_node.value} does not exist in the linked list")

def findLowestValue(head: Node):
    current_node = head
    lowest = head
    while current_node:
        if current_node.value < lowest.value:
            lowest = current_node
        current_node = current_node.next
    print(f"The lowest value is {lowest.value}")

def findHighestValue(head: Node):
    current_node = head
    highest = head
    while current_node:
        if current_node.value > highest.value:
            highest = current_node
        current_node = current_node.next
    print(f"The highest value in the linked list is {highest.value}")

def insertNode(head: Node, node_insert: Node, index_insert: int):
    if index_insert == 0:
        node_insert.next = head
        return node_insert
    current_node = head
    index = 0
    while current_node:
        if index_insert == index:
            node_insert.next = current_node
            prev_node.next = node_insert
            break
        index +=1
        prev_node = current_node
        current_node = current_node.next
    return head


def removeNode(head: Node, node_remove: Node):
    if node_remove == head:
        return head.next
    current_node = head
    while current_node:
        if current_node.next == node_remove:
            current_node.next = current_node.next.next
            return head
        current_node = current_node.next


        

#Usecase
node1 = Node(5)
node2 = Node(3)
node3 = Node(7)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

node5 = Node(9)

traverse(head=node1)
search(head=node1, search_node=node2)
search(head=node1, search_node=node5)


findLowestValue(node1)

findHighestValue(node1)

node = insertNode(head=node1, node_insert=node5, index_insert=3)
traverse(node)
node1 = removeNode(head=node1, node_remove=node4)

traverse(node1)