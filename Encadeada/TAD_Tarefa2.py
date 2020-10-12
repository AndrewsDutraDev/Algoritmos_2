def n_element(arrayList):
    size = 0
    for elemento in arrayList:
        if (elemento != None):
            size += 1        
    return size

def compare_list(arrayList, another_list):
    equallity = False
    count_equal = 0
    size_arrayList = n_element(arrayList)
    size_arrayList2 = n_element(another_list)
    if (size_arrayList == size_arrayList2):    
        for first_elem in arrayList:
            for sec_elem in another_list:
                if (first_elem == sec_elem):
                    count_equal += 1
                    if (count_equal == size_arrayList):
                        equallity = True
    return equallity

def inverter()

        
