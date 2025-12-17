def find_pairs(num_string):
    
    split_string = num_string.split()
    num_list = []
    for num in split_string:
        num_list.append(int(num))
        

    if len(num_list) < 2:
        return set()
    
    result = set()
    
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            if num_list[i] < num_list[j]:
              result.add((num_list[i], num_list[j]))
            else:
              result.add((num_list[j], num_list[i]))

       
               
    return result

           

  


# # Test cases
assert find_pairs("7 3 99") == {(7, 99), (3, 7), (3, 99)}
assert find_pairs("2 1") == {(1, 2)}
assert find_pairs("24 7 365 94") == {(7, 94), (24, 94), (94, 365), (7, 365), (24, 365), (7, 24)}
assert find_pairs("94") == set()

# print("All tests passed!")
# print("Finished early? Discuss time & space complexity")

# # typecast input into int 
# # set()
# # a loop within a loop that goes over the values in list of nums 
# # if l[i] < l[j]

# # set.add((l[i], l[j]))
# # else set.add((l[j], l[i]))
