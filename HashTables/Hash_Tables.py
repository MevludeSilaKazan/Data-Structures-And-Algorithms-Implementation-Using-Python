class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(f"Key '{key}' not found in the hash table.")

    def remove(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
        raise KeyError(f"Key '{key}' not found in the hash table.")

    def __str__(self):
        return str(self.table)


# Example usage:
if __name__ == "__main__":
    hash_table = HashTable(size=10)

    hash_table.insert("apple", 42)
    hash_table.insert("banana", 57)
    hash_table.insert("orange", 33)

    print(hash_table)  # Output: [[], [], [], [['orange', 33]], [['apple', 42]], [], [], [['banana', 57]], [], []]

    print(hash_table.get("apple"))  # Output: 42
    print(hash_table.get("banana"))  # Output: 57
    print(hash_table.get("orange"))  # Output: 33

    hash_table.remove("apple")
    print(hash_table)  # Output: [[], [], [], [['orange', 33]], [], [], [], [['banana', 57]], [], []]
