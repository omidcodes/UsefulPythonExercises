class HashTable:

    def __init__(self, size):
        self.data_map = [None] * size
    
    def __hash(self, key) -> int:
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index : int = self.__hash(key=key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self , key) -> int:
        """
        returns: index
        """

        index : int = self.__hash(key=key)
        if self.data_map[index] is None:
            return None
        
        for item in self.data_map[index]:
            if item[0] == key:
                return item[1]
        return None

    def get_keys(self) -> list:

        all_keys = []

        for index in range(len(self.data_map)):

            if self.data_map[index] is None:
                continue
            
            for item in self.data_map[index]:
                key = item[0]
                all_keys.append(key)

        return all_keys

my_hash_table = HashTable(size=7)

my_hash_table.set_item(key='Omid' , value=1000)
my_hash_table.set_item(key='Ali' , value=754)
my_hash_table.set_item(key='Jack' , value=19)

my_hash_table.print_table()
print("*" * 10)

print(my_hash_table.get_item(key='Omid'))
print(my_hash_table.get_item(key='WRONG Key'))

print("*" * 10)

print(f"Keys --> {my_hash_table.get_keys()}")
