from datetime import date, timedelta
from decimal import Decimal
from data import Holidays,HoursPerMonth
from dateutil import relativedelta

HoursPerDay = 8
HoursPerShortDay = 7
Monday = 0

class Calculator:
    def calculate(self, year:int, vacation_duration:int):
        first_day = date(year, 1, 1)
        while first_day.weekday() != Monday:
            first_day = add_days(first_day, 1)
            
        vacation_periods: dict[date, Decimal] = {}
        while first_day <= date(year, 12, 31):
            average_hourly_salary = self.get_average_hourly_salary_for_6_previous_calendar_months(first_day)
            salary_difference_during_period = self.get_salary_difference_during_period(average_hourly_salary, first_day, add_days(first_day, vacation_duration - 1))
            vacation_periods[first_day] = salary_difference_during_period
            print(f"Vacation start on {first_day}, salary difference: {salary_difference_during_period * 100}%")
            first_day = add_days(first_day, 7)
        return vacation_periods

    def get_average_hourly_salary_for_6_previous_calendar_months(self, first_day: date):
        first_day_of_month = date(first_day.year, first_day.month, 1)
        
        seven_months_ago = add_months(first_day_of_month, -7)
            
        total_hours = 0
        for i in range(0, 6):
            current_month = add_months(seven_months_ago, i)
            total_hours += HoursPerMonth[current_month.year * 100 + current_month.month]

        return Decimal(6 / total_hours)
    
    def get_salary_difference_during_period(self, average_salary_per_hour: Decimal, period_start: date, period_end: date):
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
    
def add_months(date: date, months: int) -> date:
    return date + relativedelta.relativedelta(months=months)

def is_working_day(date: date):
    return date.weekday() < 5 and date not in Holidays

def is_short_day(date: date):
    return add_days(date, 1) in Holidays

def add_days(date: date, days: int) -> date:
    return date + timedelta(days=days)