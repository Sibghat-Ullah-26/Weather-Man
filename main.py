import sys
from yearly import Yearly
from month import Month
from barchart import Barchart

if __name__ == "__main__":
    if len(sys.argv) == 4:
        output_type = sys.argv[1]
        date = sys.argv[2]
        path = sys.argv[3]

        if output_type == '-e':
            yearly_data = Yearly(date, path)
            yearly_data.calculate_year_data()
        elif output_type == '-a':
            monthly_data = Month(date, path)
            monthly_data.calculate_month_data()
        elif output_type == '-c':
            barchart_data = Barchart(date, path)
            barchart_data.create_bar_chart()
        else:
            print("Invalid output type provided.")

    else:
        print("Invalid argument length")
