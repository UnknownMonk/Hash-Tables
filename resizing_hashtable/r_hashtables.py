# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.storage = [None]*capacity
        self.capacity = capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    val = 5381
    for x in string:
        val = ((val << 5)+val)+ord(x)
    return val % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    slot = hash(key, hash_table.capacity)
    if hash_table.storage[slot] == None:
        hash_table.storage[slot] = LinkedPair(key, value)

    else:
        pair = hash_table.storage[slot]
        if pair.key == key:
            hash_table.storage[slot].value = value

        else:
            while pair.next != None:
                pair = pair.next
                if pair.key == key:
                    pair.value = value

        pair.next = LinkedPair(key, value)


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    slot = hash(key, hash_table.capacity)
    if hash_table.storage[slot] == None:
        print("No slots here")

    else:
        pair = hash_table.storage[slot]

        while pair.next != None:
            if pair.next.key == key:
                pair.next = pair.next.next

                break

        else:
            if pair.key == key:
                hash_table.storage[slot] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] != None:
        pair = hash_table.storage[index]
        while pair != None:
            if pair.key == key:
                return pair.value
            pair = pair.next


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):

    return hash_table


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
