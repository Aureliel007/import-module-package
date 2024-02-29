from datetime import datetime
import pyjokes
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(f'Current date: {datetime.now().strftime("%d/%m/%Y %H:%M")}')
    # Геренирует случайную шутку про Чака Норриса:
    print(f'Joke of the day: {pyjokes.get_joke(category="chuck")}')