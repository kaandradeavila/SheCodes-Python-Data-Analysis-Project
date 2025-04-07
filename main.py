import csv
import matplotlib.pyplot as plt

def handle_csv_file (filename):
    population_per_continent = {}

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        for line in reader:
            continent = line['continent']
            year = int(line['year'])
            population = int(line['population'])

            if continent not in population_per_continent:
                population_per_continent[continent] = {'year': [], 'population': []}
                
            population_per_continent[continent]['year'].append(year)
            population_per_continent[continent]['population'].append(population)
            

    return population_per_continent

def create_data_dictionary(reader):
    print("In progress")

    


# Open and read csv file
filename = "data.csv"
population_dictionary = handle_csv_file(filename)

# Store csv file data in dictionary

# Display plot graph