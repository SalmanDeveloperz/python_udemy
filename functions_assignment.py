"""

- Create a function that takes in 3 parameters(firstname, lastname, age) and

returns a dictionary based on those values

"""

def dict (dict_words):
    for i,j in dict_words.items():
        print(f"{i} : {j}")


my_dictinary={
    "firstname": "Salman",
    "lastname": "Ch",
    "age": "22"
}
dict(my_dictinary)