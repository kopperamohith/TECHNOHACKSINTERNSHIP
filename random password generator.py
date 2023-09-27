import random
def genpas(n):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
    pas = ""
    for i in range(n):
        pas += random.choice(characters)
    return pas
n = int(input("enter the length you need"))
password = genpas(n)
print("A generated passwaord is:", password)
