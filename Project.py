"""This program allows user to select zip codes for database"""
import csv

from enum import Enum


class Stats(Enum):
    MIN = 0
    AVG = 1
    MAX = 2


class EmptyDatasetError(Exception):
    pass


class NoMatchingItems(Exception):
    pass


filename = './purple_air.csv'


class DataSet:
    """ the DataSet class will present summary tables based on
    information imported from a .csv file
    """
    max_name_length = 30

    def __init__(self, header=""):
        self.header = header
        self._data = None
        self._zips = {}
        self._times = []

    @property
    def header(self):
        """ Return the value of the _header property """
        return self._header

    @header.setter
    def header(self, header: str):
        """ Set the value of the _header property """
        if len(header) > DataSet.max_name_length:
            raise ValueError
        else:
            self._header = header

    def _initialize_labels(self):
        """ Examine the category labels in self.__data and create a set
            for each category containing the labels
            """
        self._zips = {}
        times_of_day = set()
        for item in self._data:
            self._zips[item[0]] = True
            times_of_day.add(item[1])
        self._times = list(times_of_day)

    def load_file(self):
        """ Loads Purple Air Data into Project """

        with open(filename, 'r', newline='') as purple_air_data:
            csvreader = csv.reader(purple_air_data)
            next(csvreader)
            self._data = [(line[1], line[4], line[5]) for line in csvreader]

        line_count = 0
        for line in self._data:
            line_count += 1
        print("Number of lines loaded:", line_count)

        self._initialize_labels()

        return line_count

    def _cross_table_statistics(self, descriptor_one: str,
                                descriptor_two: str):
        """ Given a label from each category, calculate summary
        statistics for the items matching both labels.

        Keyword arguments:
            descriptor_one -- the label for zipcodes
            descriptor_two -- the label for time of day

        Returns a tuple of min, average, max from the matching rows.
        """
        if self._data is None:
            raise EmptyDatasetError

        my_list_comprehension = [float((item[2])) for item in self._data
                                 if item[0] == descriptor_one and
                                 item[1] == descriptor_two]

        if len(my_list_comprehension) == 0:
            raise NoMatchingItems

        return min(my_list_comprehension), \
            sum(my_list_comprehension)/len(my_list_comprehension),\
            max(my_list_comprehension)

    def display_cross_table(self, stat: Stats):
        """ Given a stat from DataSet.Stats, produce a table that
        shows the value of that stat for every pair of labels from the
        two categories
        """
        if self._data is None:
            print("Please Load Data First.")
            return

        filtered_zips = [item for item in self._zips.keys() if self._zips[item]
                         is True]

        print("        Morning    Midday   Evening     Night")
        for zipcode in filtered_zips:
            print(f"{zipcode:3}", end="")
            for timeofday in self._times:
                try:
                    results = self._cross_table_statistics(zipcode, timeofday)
                    print(f"{results[stat.value]:>10.2f}", end="")

                except NoMatchingItems:
                    print("       N/A", end="")
            print("")

    def get_zips(self):
        """" returns copy of zipcode dictionary """
        return self._zips.copy()

    def toggle_zip(self, target_zip: str):
        """ switches zipcode value in dictionary between true and
        false
        """
        if target_zip not in self.get_zips():
            raise LookupError
        self._zips[target_zip] = not self._zips[target_zip]


def manage_filters(my_dataset: DataSet):
    """ creates menu to select zipcodes for database """

    list_of_zips = list(my_dataset.get_zips())

    if not list_of_zips:
        print("Please Load Data First.")
        return
    else:
        while True:
            dictionary_of_zips = my_dataset.get_zips()
            print("The following labels are in the dataset.")
            for item_number, item in enumerate(list_of_zips, 1):
                print(f"{item_number}: {item}", end="")
                mode = ('ACTIVE' if dictionary_of_zips[item] else 'INACTIVE')
                print(f"{mode:>10}", end="")
                print("")

            try:
                your_answer = input("Please select an item to toggle or press "
                                    "enter/return when you are finished.")

                if your_answer == "":
                    break

                your_answer = int(your_answer)

                if your_answer == 1:
                    my_dataset.toggle_zip(list_of_zips[your_answer-1])
                    continue
                elif your_answer == 2:
                    my_dataset.toggle_zip(list_of_zips[your_answer-1])
                    continue
                elif your_answer == 3:
                    my_dataset.toggle_zip(list_of_zips[your_answer-1])
                    continue
                elif your_answer == 4:
                    my_dataset.toggle_zip(list_of_zips[your_answer-1])
                    continue
                elif your_answer == 5:
                    my_dataset.toggle_zip(list_of_zips[your_answer-1])
                    continue
                elif your_answer == 6:
                    my_dataset.toggle_zip(list_of_zips[your_answer-1])
                    continue
                elif your_answer == 7:
                    my_dataset.toggle_zip(list_of_zips[your_answer-1])
                    continue
                elif your_answer == 8:
                    my_dataset.toggle_zip(list_of_zips[your_answer-1])
                    continue
                else:
                    print("Please select a number listed in the menu.")
                    continue
            except ValueError:
                print("Please enter a number listed in the menu.")
                continue  # Restarts to the top of Loop


def menu(my_dataset: DataSet):
    """ present user with options to access the Airbnb dataset """
    print(f"{my_dataset.header}")
    print_menu()


def print_menu():
    """ Print Air Quality Database Menu """
    print("Main Menu")
    print("1 - Print Average Particulate Concentration by Zip Code and Time")
    print("2 - Print Minimum Particulate Concentration by Zip Code and Time")
    print("3 - Print Maximum Particulate Concentration by Zip Code and Time")
    print("4 - Adjust Zip Code Filters")
    print("5 - Load Data")
    print("9 - Quit")


def main():
    purple_air = DataSet()
    """ Make a Friendly Greeting """
    my_name = input("Please type in your name: ")
    print("Hello ", my_name, ", welcome to the air quality database.", sep='')

    while True:
        header = input("Enter a header for the menu: ")
        try:
            purple_air.header = header
            break

        except ValueError:
            print("Please enter a header less than or equal to 30 characters.")
            continue

    # Menu is printed in a loop to allow for other user selections
    while my_name:
        menu(purple_air)
        try:
            your_choice = int(input("what is your choice? "))
            if your_choice == 1:
                purple_air.display_cross_table(Stats.AVG)

            elif your_choice == 2:
                purple_air.display_cross_table(Stats.MIN)

            elif your_choice == 3:
                purple_air.display_cross_table(Stats.MAX)

            elif your_choice == 4:
                manage_filters(purple_air)

            elif your_choice == 5:
                purple_air.load_file()

            elif your_choice == 9:
                print("Thank you for using our database! Goodbye.")
                break  # Exits Loop
            else:
                print("Please select a number listed in the menu.")

        except ValueError:
            print("Please enter a number.")
            continue  # Restarts to the top of Loop


if __name__ == "__main__":
    main()


r"""
--- Assignment 11 Sample Run ---
Please type in your name: Cameron
Hello Cameron, welcome to the air quality database.
Enter a header for the menu: Data For A Cleaner World
Data For A Cleaner World
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
what is your choice? 1
Please Load Data First.
Data For A Cleaner World
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
what is your choice? 5
Number of lines loaded: 6147
Data For A Cleaner World
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
what is your choice? 1
        Morning    Midday   Evening     Night
94028      1.54      1.58      2.26      2.92
94304      1.36      1.23      1.17      2.89
94022      1.50      1.32      1.22      2.92
94024      1.71      1.69      3.42      3.27
94040      1.86      2.47      4.57      3.28
94087      2.24      2.31      4.77      3.92
94041      2.41      3.43      4.53      3.52
95014      1.06      2.19      2.38      3.29
Data For A Cleaner World
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
what is your choice? 2
        Morning    Midday   Evening     Night
94028      0.00      0.00      0.00      0.00
94304      0.00      0.00      0.00      0.00
94022      0.00      0.00      0.00      0.00
94024      0.00      0.00      0.00      0.00
94040      0.00      0.00      0.00      0.00
94087      0.00      0.00      0.00      0.00
94041      0.00      0.00      0.00      0.00
95014      0.00      0.00      0.00      0.00
Data For A Cleaner World
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
what is your choice? 3
        Morning    Midday   Evening     Night
94028     25.72     25.00     79.88     24.21
94304      9.66      9.92      9.73     20.93
94022     12.90     14.38     11.53     26.59
94024     15.12      9.67     37.57     29.17
94040     10.49     20.34     44.05     25.95
94087      9.39     13.14     38.11     26.48
94041      8.02     19.67     31.82     25.89
95014      9.95     37.82     69.05     25.00
Data For A Cleaner World
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
what is your choice? 4
The following labels are in the dataset.
1: 94028    ACTIVE
2: 94304    ACTIVE
3: 94022    ACTIVE
4: 94024    ACTIVE
5: 94040    ACTIVE
6: 94087    ACTIVE
7: 94041    ACTIVE
8: 95014    ACTIVE
Please select an item to toggle or press enter/return when you are finished.8
The following labels are in the dataset.
1: 94028    ACTIVE
2: 94304    ACTIVE
3: 94022    ACTIVE
4: 94024    ACTIVE
5: 94040    ACTIVE
6: 94087    ACTIVE
7: 94041    ACTIVE
8: 95014  INACTIVE
Please select an item to toggle or press enter/return when you are finished.
Data For A Cleaner World
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
what is your choice? 3
        Morning    Midday   Evening     Night
94028     25.72     25.00     79.88     24.21
94304      9.66      9.92      9.73     20.93
94022     12.90     14.38     11.53     26.59
94024     15.12      9.67     37.57     29.17
94040     10.49     20.34     44.05     25.95
94087      9.39     13.14     38.11     26.48
94041      8.02     19.67     31.82     25.89
Data For A Cleaner World
Main Menu
1 - Print Average Particulate Concentration by Zip Code and Time
2 - Print Minimum Particulate Concentration by Zip Code and Time
3 - Print Maximum Particulate Concentration by Zip Code and Time
4 - Adjust Zip Code Filters
5 - Load Data
9 - Quit
what is your choice? 9
Thank you for using our database! Goodbye.
"""