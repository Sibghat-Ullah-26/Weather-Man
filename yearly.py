import os
from date_extractor import extract_date


class Yearly:
    def __init__(self, date, path):
        self.date = date
        self.path = path

    def calculate_year_data(self):
        content = os.listdir(self.path)
        max_temp = '0'
        max_temp_date = ''
        min_temp = '0'
        min_temp_date = ''
        max_humidity = '0'
        max_humidity_date = ''
        selected_year = [x for x in content if self.date in x]
        if len(selected_year) > 0:
            for file_name in selected_year:
                try:
                    with open(os.path.join(self.path, file_name), 'r') as file:
                        for line in file.readlines():
                            file_contents = line.split(',')
                            if self.date in file_contents[0]:
                                if int(min_temp) == 0:
                                    min_temp = file_contents[3]

                                if len(file_contents[0]) > 0:

                                    if len(file_contents[1]) > 0 and int(file_contents[1]) > int(max_temp):
                                        max_temp = file_contents[1]
                                        max_temp_date = file_contents[0]
                                    if len(file_contents[3]) > 0 and int(file_contents[3]) < int(min_temp):
                                        min_temp = file_contents[3]
                                        min_temp_date = file_contents[0]
                                    if len(file_contents[7]) > 0 and int(file_contents[7]) > int(max_humidity):
                                        max_humidity = file_contents[7]
                                        max_humidity_date = file_contents[0]

                except FileNotFoundError:
                    print(f"Error: {file_name} not found.")
            max_temp_extracted_date = extract_date(max_temp_date)
            min_temp_extracted_date = extract_date(min_temp_date)
            max_humidity_extracted_date = extract_date(max_humidity_date)
            print(f"Highest: {max_temp}C on {max_temp_extracted_date[0]} {max_temp_extracted_date[1]}")
            print(f"Lowest: {min_temp}C on {min_temp_extracted_date[0]} {min_temp_extracted_date[1]}")
            print(f"Humid: {max_humidity}% on {max_humidity_extracted_date[0]} {max_humidity_extracted_date[1]}")
        else:
            print(f"Couldn't found selected year: {self.date}")
