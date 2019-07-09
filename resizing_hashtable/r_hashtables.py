

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"{self.key}, {self.value}"

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

def hash(string, max):
    hash = 5381
    for char in string:
        hash = (hash * 33) + ord(char)
    return hash % max

def hash_table_insert(hash_table, key, value):
    new_element = LinkedPair(key, value)
    index = hash(key, hash_table.capacity)
    bucket = hash_table.storage[index]
    if bucket is not None:
        if new_element.key == bucket.key:
            print('Overwriting existing pair')
            hash_table.storage[index] = new_element
        elif new_element.key != bucket.key:
            if bucket.next == None:
                bucket.next = new_element
            else:
                while bucket.next != None:
                    bucket = bucket.next
                    if bucket.next == None:
                        bucket.next = new_element
                        break
    else:
        hash_table.storage[index] = new_element

def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    bucket = hash_table.storage[index]
    if bucket:
        if bucket.key == key:
            hash_table.storage[index] = None
        else:
            while bucket.next != None:
                bucket = bucket.next
                if bucket.key == key:
                    bucket = None
                    break
    else:
        print("That element does not exist")


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    bucket = hash_table.storage[index]
    if bucket:
        if bucket.key == key:
            return bucket.value
        else:
            while bucket.next != None:
                bucket = bucket.next
                if bucket.key == key:
                    return bucket.value
    else:
        print("Element does not exist")
        return None

# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    new_storage = [None] * hash_table.capacity
    hash_table.storage.extend(new_storage)
    return hash_table.storage


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
