#Names: Aamir Kapasi and Lucille Sanders
#emails: akapasi@umich.edu and lucysand@umich.edu
#UMIDs: 75001048 and 84724442
#collaborators: COPilot
    #worked with to debug code and helped write some of our 
    #functions like generate_report for formatting and writing. Also helped write 
    #our test cases which we then edited to match the data incosistencies it couldn't forsee.
#functions created by each student: 
#Aamir: Load_penguins, year_body_mass_dict
#Lucy: avg_body_mass_island, avg_body_mass_year, generate_report

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
    


def generate_report(avg_body_mass_island, avg_body_mass_year):
    avg_body_mass_year = avg_body_mass_year()
    avg_body_mass_island = avg_body_mass_island()
    lines = []
    lines.append("Penguin Body Mass Report\n")
    for year in avg_body_mass_year:
        lines.append(f"Year: {year}\n")
        lines.append(f"  Average body mass: {avg_body_mass_year[year]}\n")
        for island in avg_body_mass_island.get(year, {}):
            island_avg = avg_body_mass_island[year][island]
            status = "above" if island_avg > avg_body_mass_year[year] else "below"
            lines.append(f"  Island: {island}, Average: {island_avg}, {status} year average\n")
        lines.append("\n")
    with open("penguin_report.txt", "w") as f:
        f.writelines(lines)
    return "Report written to penguin_report.txt"

def main():
    generate_report(avg_body_mass_island, avg_body_mass_year)

main()

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

class TestYearBodyMassDict(unittest.TestCase):
    def test_known_year_island(self):
        result = year_body_mass_dict()
        self.assertIn('"Torgersen"', result[2007])
        self.assertEqual(result[2007]['"Torgersen"'][0], 3750)
    def test_year_contains_islands(self):
        result = year_body_mass_dict()
        self.assertIn('"Biscoe"', result[2008])
        self.assertIn('"Dream"', result[2008])
    def test_year_not_in_data(self):
        with self.assertRaises(KeyError):
            year_body_mass_dict()[9999]
    def test_empty_data(self):
        def mock_load_penguins(filename):
            return {}
        original = load_penguins
        try:
            globals()['load_penguins'] = mock_load_penguins
            self.assertEqual(year_body_mass_dict(), {})
        finally:
            globals()['load_penguins'] = original

class TestAvgBodyMassIsland(unittest.TestCase):
    def test_known_year_island_average(self):
        result = avg_body_mass_island()
        self.assertAlmostEqual(result[2007]['"Torgersen"'], 3763.16, places=2)
    def test_all_islands_have_averages(self):
        result = avg_body_mass_island()
        for island in result[2008]:
            self.assertIsInstance(result[2008][island], float)
    def test_year_not_in_data(self):
        result = avg_body_mass_island()
        with self.assertRaises(KeyError):
            _ = result[9999]
    def test_empty_data(self):
        def mock_year_body_mass_dict():
            return {}
        original = year_body_mass_dict
        try:
            globals()['year_body_mass_dict'] = mock_year_body_mass_dict
            self.assertEqual(avg_body_mass_island(), {})
        finally:
            globals()['year_body_mass_dict'] = original

class TestAvgBodyMassYear(unittest.TestCase):
    def test_known_year_average(self):
        result = avg_body_mass_year()
        self.assertAlmostEqual(result[2007], 4124.54, places=2)
    def test_all_years_have_averages(self):
        result = avg_body_mass_year()
        for year in result:
            self.assertIsInstance(result[year], float)
    def test_year_not_in_data(self):
        result = avg_body_mass_year()
        with self.assertRaises(KeyError):
            _ = result[9999]
    def test_empty_data(self):
        def mock_year_body_mass_dict():
            return {}
        original = year_body_mass_dict
        try:
            globals()['year_body_mass_dict'] = mock_year_body_mass_dict
            self.assertEqual(avg_body_mass_year(), {})
        finally:
            globals()['year_body_mass_dict'] = original

class TestGenerateReport(unittest.TestCase):
    def test_report_file_created(self):
        import os
        if os.path.exists("penguin_report.txt"):
            os.remove("penguin_report.txt")
        generate_report(avg_body_mass_island, avg_body_mass_year)
        self.assertTrue(os.path.exists("penguin_report.txt"))
    def test_report_content(self):
        generate_report(avg_body_mass_island, avg_body_mass_year)
        with open("penguin_report.txt", "r") as f:
            content = f.read()
        self.assertIn("Penguin Body Mass Report", content)
        self.assertIn("Year: 2007", content)
        self.assertIn("Island: \"Torgersen\"", content)

unittest.main()
if __name__ == "__main__":
    
    unittest.main()

