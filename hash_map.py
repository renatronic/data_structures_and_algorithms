class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)] # creates a list of size array_size and makes every element of .array equal to None

  def hash(self, key, count_collisions=0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value): # the setter
    array_index = self.compressor(self.hash(key)) # plugs the key into the .hash() method and then the hash code into the .compressor() method
    # self.array[array_index] = value # not necessary since it's replaced by collision detectors below
    current_array_value = self.array[array_index] # saves the value to the map’s array at the index determined previously

    if current_array_value is None:
      self.array[array_index] = [key, value]
      return

    if current_array_value[0] == key: # remember, current_array_value actually holds our key/value pairs in an array that looks like [key, value]
      self.array[array_index] = [key, value] # so to check if the keys are equal, you should compare key to current_array_value[0]
      return

    # Collision!

    number_collisions = 1 # unnecessary to add an else statement

    while(current_array_value[0] != key): # here we want to replicate our setting logic while incrementing the number of collisions
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array[new_array_index]

      if current_array_value is None:
        self.array[new_array_index] = [key, value]
        return

      if current_array_value[0] == key:
        self.array[new_array_index] = [key, value]
        return

      number_collisions += 1 # unnecessary to add an else statement

    return

  def retrieve(self, key):  # the getter
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index] # save the array value at our compressed hash code into possible_return_value

    if possible_return_value is None:
      return None

    if possible_return_value[0] == key:
      return possible_return_value[1]

    retrieval_collisions = 1

    while (possible_return_value != key): # in this while loop, we want to replicate our retrieval logic while increasing the count of retrieval_collisions so that we continue to look at other locations within our array
      new_hash_code = self.hash(key, retrieval_collisions)
      retrieving_array_index = self.compressor(new_hash_code)
      possible_return_value = self.array[retrieving_array_index]

      if possible_return_value is None:
        return None

      if possible_return_value[0] == key:
        return possible_return_value[1]

      retrieval_collisions += 1

    return


'''
Things to consider about the hash map data structure above:

1. Notice that it does not work if we want to delete keys.
How would you delete a key-value pair from this hash map?

2. Parts of the code are a little repetitive, how would you factor these roles differently?

3. What should your hash map do if a key-value is added and the array is full? How does this hash map handle that?
'''