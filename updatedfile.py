#Names: Aamir Kapasi and Lucille Sanders
#emails: akapasi@umich.edu and lucysand@umich.edu
#UMIDs: 75001048 and 84724442
#collaborators: 
#functions created by each student:
#Aamir:
#Lucy:
def load_penguins(filename):
    with open(filename, "r") as f:
        file = f.readlines()
        main_penguin_dict={}
        for i in file[1:]:
            text = i.split(",")
            try:
                main_penguin_dict[text[0]] =[text[2],int(text[6]),int(text[8].strip())]
            except:
                continue
    return main_penguin_dict
load_penguins("penguins.csv")



#[year][penguin] = [body_mass_g, island]