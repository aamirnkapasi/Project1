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
        penguins={}
        for i in file[1:]:
            text = i.split(",")
            try:
                penguins[text[0]] =[text[2],int(text[6]),int(text[8].strip())]
            except:
                continue
    return penguins

def year_body_mass_dict():
    penguins = load_penguins("penguins.csv")
    year_body_mass = {}
    for key, val in penguins.items():
        island = val[0]
        body_mass = val[1]
        year = val[2]
        if year not in year_body_mass:
            year_body_mass[year] = {}
        if island not in year_body_mass[year]:
            year_body_mass[year][island] = []
        year_body_mass[year][island].append(body_mass)
    return year_body_mass
        

def avg_body_mass_island():
    year_body_mass = year_body_mass_dict()
    avg_body_mass = {}
    for year in year_body_mass:
        avg_body_mass[year] = {}
        for island in year_body_mass[year]:
            body_masses = year_body_mass[year][island]
            if body_masses:
                avg_mass = sum(body_masses) / len(body_masses)
                avg_body_mass[year][island] = round(avg_mass,2)
    return avg_body_mass

def avg_body_mass_year():
    year_body_mass = year_body_mass_dict()
    avg_body_mass_year = {}
    for year in year_body_mass:
        total_mass = 0
        count = 0
        for island in year_body_mass[year]:
            body_masses = year_body_mass[year][island]
            total_mass += sum(body_masses)
            count += len(body_masses)
        if count > 0:
            avg_body_mass_year[year] = round(total_mass / count, 2)
        else:
            avg_body_mass_year[year] = None
    return avg_body_mass_year
    

print(avg_body_mass_year())




#[year][penguin] = [body_mass_g, island]


import unittest
class TestLoadPenguins(unittest.TestCase):
    def test_load_penguins(self):
        self.assertEqual(load_penguins("penguins.csv")['"1"'], ['"Torgersen"', 3750, 2007])
        self.assertEqual(load_penguins("penguins.csv")['"2"'], ['"Torgersen"', 3800, 2007])
        self.assertFalse(load_penguins("penguins.csv")['"3"'] == ['"Torgersen"', 3250, 2009])
        self.assertFalse(len(load_penguins("penguins.csv")) == 343)
        data = {"'4'":['"Torgersen"', 'NA', '2007']}
        with self.assertRaises(KeyError):
            load_penguins("penguins.csv")['"4"'] == data["'4'"]

unittest.main()
if __name__ == "__main__":
    unittest.main()
