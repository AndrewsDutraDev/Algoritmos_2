
class PilhaEnc:
    def __init__(self):
        self.vector = [None]
        self.top = -1
        self.base = 0

    def insert_top(self, value):
        counter = 0
        for x in self.vector:
            counter += 1
        new_size = counter + 1
        vector_helper = self.vector
        self.vector = [None] * new_size
        for x in range(0, counter):
            self.vector[x] = vector_helper[x]
        self.vector[self.top] = ('<--', value)
            
    def remove_top(self):
        counter = 0
        for x in self.vector:
            counter += 1
        if counter == 1:
            return
        else:
            new_size = counter - 1
            vector_helper = self.vector
            self.vector = [None] * new_size
            for x in range(0, counter - 1):
                self.vector[x] = vector_helper[x]

    def query(self):
        if self.vector[self.base] == self.vector[self.top]:
            return
        else:
            return self.vector[self.top][1]

    def destroy(self):
        self.vector = [None]
    
    def get_list(self):
        return self.vector
    
    def compare(self, list_one, list_two):
        counter_listone = 0
        for x in list_one:
            counter_listone += 1
        counter_listtwo = 0
        for x in list_two:
            counter_listtwo += 1
        equallity = True
        if counter_listone != counter_listtwo:
            equallity = False
        else:
            for x in range(0, counter_listone):
                if list_one[x] != list_two[x]:
                    equallity = False
        return equallity