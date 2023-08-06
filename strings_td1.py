# Create a function that, given a string, returns all of that string’s contents, but without blanks.If given the string " Pl ayTha tF u nkyM usi c ", return "PlayThatFunkyMusic"
def remove_blanks(str):
    # creating new empty string to add letters to
    str2 = ""
    # for loop to check the value of each character in the original string
    for i in str:
        # if statement to check if the character is blank, if its not, it puts it in the new string
        if not i == " ":
            str2 += i
    # return statement returning the new string
    return str2

print(remove_blanks("Pl ayTha tF u nkyM usi c "))

# Create a function that given a string, returns the integer made from the string’s digits. Given "0s1a3y5w7h9a2t4?6!8?0", the function should return the number 1357924680.
def get_digits(str):
    # create empty string to add to
    str2 = ""
    # for loop to iterate through the string
    for i in str:
        # series of if statements to catch if it is a number in string form, if it is, it adds it to the new string
        if i == "1":
            str2 += i
        if i == "2":
            str2 += i
        if i == "3":
            str2 += i
        if i == "4":
            str2 += i
        if i == "5":
            str2 += i
        if i == "6":
            str2 += i
        if i == "7":
            str2 += i
        if i == "8":
            str2 += i
        if i == "9":
            str2 += i
        if i == "0":
            str2 += i
    # return statement for the new string
    return str2

print(get_digits("0s1a3y5w7h9a2t4?6!8?0"))

# Create a function that, given a string, returns the string’s acronym (first letters only, capitalized). Given " there's no free lunch - gotta pay yer way. ", return "TNFL-GPYW" Given "Live from New York, it's Saturday Night!", return "LFNYISN".
def acronyms(str):
    # spliting the words in the original string into a dictionary
    str2 = str.split()
    # setting up the acronym variable to add to
    acronym = ""
    # for loop to iterate through the dictionary
    for i in str2:
        # storing only the first index of each item in the dictionary,and making it uppercase
        acronym += i[0].upper()
    # return statement for the new string
    return acronym

print(acronyms("there's no free lunch - gotta pay yer way"))
print(acronyms("Live from New York, it's Saturday Night!"))

# Given two arrays, create an associative array (map) containing keys of the first, and values of the second. For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true], return {"abc": 42, 3: "wassup", "yo": true}.
def zip_arrays(arr1, arr2):
    # setting up empty map/dictionary
    map = {}
    # for loop to iterate through the range of the first array to match with the things associated with it in the second
    for i in range(len(arr1)):
        # taking the valiue of the index of arr1, converting it to a string to be the key and adding the value that matches that same index in arr2
        map[str(arr1[i])] = arr2[i]
    # return statement for the map
    return map

print(zip_arrays(["abc", 3, "yo"], [42, "wassup", True]))

#  Build invertHash(assocArr) to convert hash keys to values, and values to keys. Example: given {"name": "Zaphod", "charm": "high", "morals": "dicey"}, return object {"Zaphod": "name", "high":"charm", "dicey": "morals"}.
def invert_hash(map1):
    # creating second map to add things to
    map2 = {}
    # for loop reading the items key and value tuples using .items()
    for key, value in map1.items():
        # adding the values into the new map, but swapping the value and key items
        map2[value] = key
    # return statement
    return map2

print(invert_hash({"name": "Zaphod", "charm": "high", "morals": "dicey"}))