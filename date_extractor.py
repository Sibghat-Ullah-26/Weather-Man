from datetime import datetime
import calendar


def extract_date(date):
    date_object = datetime.strptime(date, "%Y-%m-%d")

    month = date_object.strftime("%B")
    day = date_object.day
    return [month, day]


def convert_to_year_month_names(year_month_string):
    try:
        year, month = map(int, year_month_string.split('/'))
        if 0 < month < 13:
            month_name = calendar.month_name[month]

            return f"{year}_{month_name[0:3]}"
        else:
            print("Month out of range")
    except ValueError:
        return None
