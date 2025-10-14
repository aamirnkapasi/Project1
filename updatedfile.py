#This is Aamir and Lucy's Project 1 on penguins
def opencsv(filename):
    with open(filename, "r") as f:
        file = f.read()
    return file
    
text = opencsv("penguins.csv")
print(text)
print(text)
