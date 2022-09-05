#Binary search

def find(search_list, value):
    
    mid = len(search_list) // 2
    
    if(len(search_list) < 1):
        raise ValueError("value not in array")
    
    if(value == search_list[mid]):
        return mid 
    elif(value < search_list[mid]):
        return find(search_list[:mid], value)
    else:
        return 1 + mid + find(search_list[mid+1:], value)