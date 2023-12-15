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
            # print(candy + " is a possible match")
    return counter
    

candies = {"candy1" : 1, "candy2" : 2, "candy3" : 3, "candy4" : 4, "candy5" : 5,
           "candy6" : 6, "candy7" : 7, "candy8" : 8, "candy9" : 9, "candy10" : 10}
# names = "candy1 candy2 candy3 candy6 candy6 candy6 candy7 candy7 candy10"
print(count_candies(candies, "./candies.txt", 5))