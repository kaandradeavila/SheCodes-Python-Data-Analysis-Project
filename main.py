import csv
import matplotlib.pyplot as plt

def handle_csv_file (filename):
    """
    This function handles the csv file with the data to be used for the project
    It opens the file, reads it, and returns a dictionary with all the data.
    """

    # Initializing dictonary that will store data from CSV file
    population_per_continent = {}

    # Open CSV file
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        # Read CSV file
        for line in reader:
            continent = line['continent']
            year = int(line['year'])
            population = int(line['population'])

            # Store CSV file data in a dictionary
            if continent not in population_per_continent:
                population_per_continent[continent] = {'years': [], 'population': []}
                
            population_per_continent[continent]['years'].append(year)
            population_per_continent[continent]['population'].append(population)
            

    return population_per_continent

def display_data_in_plot_graph(population_per_continent_dictionary):
    """
    Obtains data from a dictionary and displays it on a plot graph.
    In this case, we are displaying the growth of Internet users in different continents
    """
  # Reading data in dictionary
    for continent in population_per_continent_dictionary:
        years = population_per_continent_dictionary[continent]['years']
        population = population_per_continent_dictionary[continent]['population']

        # Plotting data on the graph
        plt.plot(years, population, label=continent, marker='o')
    
    # General plot graph styling (title, legend, labels...)
    plt.title("Growth of Internet Users per Continent")
    plt.legend()
    plt.grid()
    plt.xlabel("Years")
    plt.ylabel("Population (in Billions)")
    plt.tight_layout()

    # Visualizing plot graph
    plt.show()


# Open, read and store csv file data in dictionary
filename = "data.csv"
population_dictionary = handle_csv_file(filename)

# Display plot graph
display_data_in_plot_graph(population_dictionary)