MATRIX = [
    [-1, -5, -47, -8, -1],
    [-4, -98, -90, -45, -78],
    [-3, -2, -5, -9, -4],
    [-8, -67, -33, -91, -40],
    [-2, -58, -11, -65, -77]
]

###         TASK 1
def sort_columns(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for col in range(cols):
        for i in range(rows - 1):
            for j in range(rows - 1 - i):
                if matrix[j][col] < matrix[j + 1][col]:
                    temp = matrix[j][col]
                    matrix[j][col] = matrix[j + 1][col]
                    matrix[j + 1][col] = temp

    return matrix

def calculate_fi(matrix):
    n = len(matrix)
    fi = []

    for i in range(1, n):
        product = 1
        for j in range(n - i, n):
            product = product * matrix[i][j]

        fi.append(product)

    return fi

def calculate_F(fi):
    total = 0
    for i in range(len(fi)):
        total = total + fi[i]

    return total / len(fi)

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]:6}", end="")

        print()

###             TASK 2
class Node:

    def __init__(self, name):
        self.name = name
        self.next = None

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head == None:
            return True

        return False

    def enqueue(self, name):
        node = Node(name)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.is_empty():
            return None

        name = self.head.name
        self.head = self.head.next

        if self.head == None:
            self.tail = None

        return name

    def print_queue(self):
        current = self.head

        while current != None:
            print(current.name, end=" ")
            current = current.next

        print()

class Supermarket:

    def __init__(self, checkouts_count: int = 1):
        self.checkouts = []

        for _ in range(checkouts_count):
            self.checkouts.append(Queue())

    def add_customer(self, name, number):
        self.checkouts[number - 1].enqueue(name)
        print(f"{name} стає в чергу на касу №{number}")

    def serve(self, number):
        name = self.checkouts[number - 1].dequeue()

        if name == None:
            print(f"Каса №{number}: черга порожня")
        else:
            print(f"Каса №{number} обслужила: {name}")

    def print_info(self):
        for i in range(len(self.checkouts)):
            print(f"Каса №{i + 1}: ", end="")
            self.checkouts[i].print_queue()

def main():
    print("\t task1")
    print("Початкова матриця:")
    print_matrix(MATRIX)

    sort_columns(MATRIX)
    
    print("\nВідсортована матриця:")
    print_matrix(MATRIX)

    fi = calculate_fi(MATRIX)
    print('\n')
    for i in range(len(fi)):
        print(f"f{i + 2} = {fi[i]}")

    F = calculate_F(fi)
    print(f"\nF = {F}")

    print("\n\t task2")
    supermarket = Supermarket(3)

    supermarket.add_customer("Олена", 1)
    supermarket.add_customer("Іван", 2)
    supermarket.add_customer("Марія", 3)
    supermarket.add_customer("Петро", 1)
    supermarket.add_customer("Анна", 2)

    print('\n')
    supermarket.print_info()
    print('\n')

    supermarket.serve(1)
    supermarket.serve(2)
    supermarket.serve(3)
    supermarket.serve(3)

    print('\n')
    supermarket.print_info()

if __name__ == "__main__":
    main()