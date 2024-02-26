import os
from date_extractor import convert_to_year_month_names


class Barchart:
    def __init__(self, date, path):
        self.date = date
        self.path = path

    def create_bar_chart(self):
        content = os.listdir(self.path)
        max_temp = '0'
        min_temp = '0'
        plus = '+'
        converted_date = convert_to_year_month_names(self.date)
        if converted_date is not None:
            selected_month = [x for x in content if converted_date in x]
            if len(selected_month) > 0:
                selected_month = selected_month[0]
                try:
                    with open(os.path.join(self.path, selected_month), 'r') as file:
                        for line in file.readlines():
                            file_contents = line.split(',')
                            if converted_date[0:4] in file_contents[0]:

                                if len(file_contents[0]) > 0:

                                    if len(file_contents[1]) > 0:
                                        max_temp = file_contents[1]
                                    if len(file_contents[3]) > 0:
                                        min_temp = file_contents[3]
                                    max_temp_stars = plus * int(max_temp)
                                    min_temp_stars = plus * int(min_temp)
                                    print(
                                        f"\033[37m{file_contents[0][-2:]}: \033[34m{min_temp_stars}"
                                        f"\033[31m{max_temp_stars} \033[37m{min_temp}C-{max_temp}C ")

                except FileNotFoundError:
                    print(f"Error: {selected_month} not found.")
            else:
                print("Couldn't found selected month")
        else:
            print("Please enter a correct date")
