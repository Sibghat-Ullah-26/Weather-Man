import os
from date_extractor import convert_to_year_month_names


def calculate_average(array):
    sum_of_items = sum(int(num) for num in array)
    average = int(sum_of_items / len(array))
    return average


class Month:
    def __init__(self, date, path):
        self.date = date
        self.path = path

    def calculate_month_data(self):
        content = os.listdir(self.path)
        avg_max_temp = []
        avg_min_temp = []
        avg_humidity = []
        converted_date = convert_to_year_month_names(self.date)
        if converted_date is not None:
            selected_month = [x for x in content if converted_date in x]
            print(selected_month)
            if len(selected_month) > 0:
                selected_month = selected_month[0]
                try:
                    with open(os.path.join(self.path, selected_month), 'r') as file:
                        for line in file.readlines():
                            file_contents = line.split(',')
                            if converted_date[0:4] in file_contents[0]:

                                if len(file_contents[0]) > 0:

                                    if len(file_contents[1]) > 0:
                                        avg_max_temp.append(file_contents[1])
                                    if len(file_contents[3]) > 0:
                                        avg_min_temp.append(file_contents[3])
                                    if len(file_contents[7]) > 0:
                                        avg_humidity.append(file_contents[7])

                except FileNotFoundError:
                    print(f"Error: {selected_month} not found.")

                print(f"Highest Average: {calculate_average(avg_max_temp)}C ")
                print(f"Lowest Average: {calculate_average(avg_min_temp)}C ")
                print(f"Average Humidity: {calculate_average(avg_humidity)}% ")
            else:
                print("Couldn't found selected month")
        else:
            print("Please enter a correct date")
