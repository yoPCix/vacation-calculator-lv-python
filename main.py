import csv
from datetime import date, timedelta
from decimal import Decimal
from calculator import calculate_by_hours, calculate_by_days
import numpy as np
from data import MonthNames

def main():
    year = 2025
 
    vacations_periods = calculate_by_hours(year, 14)
    generate_csv(year, vacations_periods)
    
    monthly_vacation_rates = calculate_by_days(year)
    generate_daily_csv(year, monthly_vacation_rates)

def generate_csv(year, vacations_periods: dict[date, Decimal]):
    with open(f"vacation_{year}_hourly.csv", "w", newline='') as file:
        writer = csv.writer(file, dialect="excel", delimiter=";")
        fields = [year] + list(range(1, 12+1))
        writer.writerow(fields)
        for day in range(1, 31+1):
            values = [day] + [get_current_rate(vacations_periods, year, month, day) for month in range(1, 12+1)]
            writer.writerow(values)
   
def generate_daily_csv(year, vacations_periods: dict[date, Decimal]):
    with open(f"vacation_{year}_daily_simple.csv", "w", encoding='utf-8', newline='') as file:
        writer = csv.writer(file, dialect="excel", delimiter=";")
        fields = [year, "atšķirība"]
        writer.writerow(fields)
        for month in range(1, 12+1):
            values = [MonthNames[month], vacations_periods[date(year, month, 1)]]
            writer.writerow(values)
             
def get_current_rate(vacations_periods: dict[date, Decimal], year, month, day):
    try:
        current_date = date(year, month, day)
        if (current_date in vacations_periods):
            return f"{vacations_periods[current_date]:.2%}"
    except:
        return ""
    return ""

if __name__ == "__main__":
    main()
