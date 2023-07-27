class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(f"Key '{key}' not found in the linked list.")

    def remove(self, key):
        if not self.head:
            raise KeyError(f"Key '{key}' not found in the linked list.")

        if self.head.key == key:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next

        raise KeyError(f"Key '{key}' not found in the linked list.")

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(f"({current.key}: {current.value})")
            current = current.next
        return " -> ".join(values)


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [LinkedList() for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        self.table[index].insert(key, value)

    def get(self, key):
        index = self._hash(key)
        return self.table[index].search(key)

    def remove(self, key):
        index = self._hash(key)
        self.table[index].remove(key)

    def __str__(self):
        return str([str(llist) for llist in self.table])


# Example usage:
if __name__ == "__main__":
    hash_table = HashTable(size=10)

    hash_table.insert("apple", 42)
    hash_table.insert("banana", 57)
    hash_table.insert("orange", 33)

    print(hash_table)
    # Output: ['None', 'None', '(orange: 33)', 'None', 'None', '(apple: 42)', '(banana: 57)', 'None', 'None', 'None']

    print(hash_table.get("apple"))  # Output: 42
    print(hash_table.get("banana"))  # Output: 57
    print(hash_table.get("orange"))  # Output: 33

    hash_table.remove("apple")
    print(hash_table)
    # Output: ['None', 'None', '(orange: 33)', 'None', 'None', 'None', '(banana: 57)', 'None', 'None', 'None']
