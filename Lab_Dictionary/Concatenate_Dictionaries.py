##2.Write a Python script to concatenate the following dictionaries to create a new one.
##  Sample Dictionary :
##
##  dic1={1:10, 2:20}
##  dic2={3:30, 4:40}
##  dic3={5:50,6:60}
##
##  Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def Concatenate_Dictionaries(*dicts):
    result = {}
    for dictionary in dicts:
        result.update(dictionary)
    return result

# Sample dictionaries

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result = Concatenate_Dictionaries(dic1, dic2, dic3)
print("Concatenated Dictionary : ",result)
