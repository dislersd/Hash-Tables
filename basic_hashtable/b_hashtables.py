

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    # def __repr__(self):
    #     return f'{self.value}'


# '''
# Basic hash table
# Fill this in.  All capacity values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    def __repr__(self):
        return f'{self.storage}'


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for char in string:
        hash = (hash * 33) + ord(char)
    return hash % max

# If you are overwriting a value with a different key, print a warning.
# '''


def hash_table_insert(hash_table, key, value):
    new_element = Pair(key, value)
    index = hash(key, hash_table.capacity)
    stored_pair = hash_table.storage[index]
    if hash_table.storage[index]:
        if new_element.key == stored_pair.key:
            print("OVERWRITING A VALUE")
    hash_table.storage[index] = new_element
    return new_element


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index].key:
        hash_table.storage[index].key = None
    else:
        print("Element does not exist")


# Should return None if the key is not found.
# '''

def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    value = hash_table.storage[index]
    if value:
        if value.key == key:
            return value.value
        else:
            return None


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()

# ht = BasicHashTable(10)
# hash_table_insert(ht, "hello", "dylan")
# hash_table_insert(ht, "yo", "berk")
# hash_table_insert(ht, "sup", "tricia")
# print(hash_table_retrieve(ht, "hello"))
