def count_candies(candies, filepath, min) -> int:
    counter = 0
    try:
        words_file = open(filepath, "r")
        words = words_file.read()
    except FileNotFoundError:
        print("FILE NOT FOUND")
        return 0
    for candy, price in candies.items():
        if price > min:
            counter += words.count(candy)
            print(candy + " is a possible match")
    return counter
    

candies = {"candy1" : 1, "candy2" : 2, "candy3" : 3, "candy4" : 4, "candy5" : 5,
           "candy6" : 6, "candy7" : 7, "candy8" : 8, "candy9" : 9, "candy10" : 10}
# names = "candy1 candy2 candy3 candy6 candy6 candy6 candy7 candy7 candy10"
# print(count_candies(candies, "./candies.txt", 5))
words_file = open("candies.txt", "r")

# ######
# def count_keys(dict, filepath, min) -> int:
    
#     try:
#         words_file = open(filepath, "r")
#         words = words_file.read().split(', ') #get list of comma separated words
#     except FileNotFoundError:
#         return 0

#     for word in words:
#         if(dict.has_key(word)


# # 2 ways to search dictionary:
# # 1) get list of keys, then for each key dict.get(key)
#     for key in dict.keys():
#            value = dict.get(key)
# # 2) get list of key-value pairs:
#     for key, value in dict.items():
#         #dict.get(key) -> returns value
#         #key - refers to some key in dict.keys()
#         #we also get value without having to call dict.get(key