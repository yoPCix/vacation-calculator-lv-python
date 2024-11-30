from datetime import date, timedelta
from decimal import Decimal
from data import Holidays,HoursPerMonth
from dateutil import relativedelta
import math

HoursPerDay = 8
HoursPerShortDay = 7
Monday = 0

def calculate_by_hours(year:int, vacation_duration:int):
    first_day = date(year, 1, 1)
    while first_day.weekday() != Monday:
        first_day = add_days(first_day, 1)
        
    vacation_periods: dict[date, Decimal] = {}
    while first_day <= date(year, 12, 31):
        average_hourly_salary = get_average_hourly_salary_for_6_previous_calendar_months(first_day)
        salary_difference_during_period = get_hourly_salary_difference_during_period(average_hourly_salary, first_day, add_days(first_day, vacation_duration - 1))
        vacation_periods[first_day] = salary_difference_during_period
        print(f"Vacation start on {first_day}, salary difference: {salary_difference_during_period * 100}%")
        first_day = add_days(first_day, 7)
    return vacation_periods

def get_average_hourly_salary_for_6_previous_calendar_months(first_day: date):
    first_day_of_month = date(first_day.year, first_day.month, 1)
    
    six_months_ago = add_months(first_day_of_month, -6)
        
    total_hours = 0
    for i in range(0, 6):
        current_month = add_months(six_months_ago, i)
        total_hours += HoursPerMonth[current_month.year * 100 + current_month.month]

    return Decimal(6 / total_hours)

def get_hourly_salary_difference_during_period(average_salary_per_hour: Decimal, period_start: date, period_end: date):
    total_salary:Decimal = 0
    current_date = period_start
    working_days = 0
    while current_date <= period_end:
        if is_working_day(current_date):
            working_days += 1
            hours_today = HoursPerShortDay if is_short_day(current_date) else HoursPerDay
            current_hours_per_month = HoursPerMonth[current_date.year * 100 + current_date.month]
            normal_hours = current_hours_per_month - hours_today
            total_salary += Decimal(normal_hours / current_hours_per_month) + Decimal(hours_today * average_salary_per_hour)
        current_date += timedelta(days=1)
    return Decimal(total_salary - working_days + 1)



def calculate_by_days(year:int):
    vacation_periods: dict[date, Decimal] = {}
    for month in range(1, 13):
        first_day = date(year, month, 1)
        average_daily_salary = get_average_daily_salary_for_6_previous_calendar_months(year, month)
        salary_difference_during_period = get_daily_salary_difference_in_month(average_daily_salary, year, month)
        vacation_periods[first_day] = salary_difference_during_period
        print(f"Vacation day in {first_day.strftime('%B')}, salary difference: {salary_difference_during_period * 100}%")
    return vacation_periods

def get_average_daily_salary_for_6_previous_calendar_months(year: int, month: int):
    first_day_of_month = date(year, month, 1)
    
    six_months_ago = add_months(first_day_of_month, -6)
    print(f"Calculating average daily salary for {year}-{month}, Six months ago: {six_months_ago}")
    total_days = 0
    for i in range(0, 6):
        current_month = add_months(six_months_ago, i)
        print (f"{current_month.month}: {workdays_per_month(current_month.year, current_month.month)}")
        total_days += workdays_per_month(current_month.year, current_month.month)
    print (f"Total working days in last 6 months: {total_days}, average daily salary: {Decimal(6 / total_days)}")
    return Decimal(6 / total_days)

 
def get_daily_salary_difference_in_month(average_salary_per_day: Decimal, year: int, month: int):
    total_salary:Decimal = 1
    working_days = workdays_per_month(year, month)
    expected_daily_rate = Decimal(1 / working_days)
    print(f"Expected daily rate: {expected_daily_rate}")
    return Decimal(average_salary_per_day / expected_daily_rate)
    
   
def add_months(date: date, months: int) -> date:
    return date + relativedelta.relativedelta(months=months)

def is_working_day(date: date):
    return date.weekday() < 5 and date not in Holidays

def is_short_day(date: date):
    return add_days(date, 1) in Holidays

def add_days(date: date, days: int) -> date:
    return date + timedelta(days=days)

def workdays_per_month(year: int, month: int):
    return sum(1 for day in range(1, 31+1) if is_valid_date(year, month, day) and is_working_day(date(year, month, day)))

def is_valid_date(year: int, month: int, day: int):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False