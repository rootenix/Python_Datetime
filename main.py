from datetime import datetime, date

members = [
    ("Aziza", "15.03.2001"),
    ("Bobur", "28.10.1995"),
    ("Dilnoza", "13.10.2008"),
    ("Eldor", "02.01.1999"),
]

def calculate_age(birth_date: date, today: date) -> int:
    yosh = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        yosh -= 1 
    return yosh

def days_until_birthday(birth_date: date, today: date) -> int:
    next_bd = birth_date.replace(year=today.year)       
    if next_bd < today:                                
        next_bd = next_bd.replace(year=today.year + 1) 
    return (next_bd - today).days                      

def report(members, today):
    print(f"--- {today.strftime('%d.%m.%Y')} ---")
    for name, birth in members:
        bd = datetime.strptime(birth, "%d.%m.%Y").date()
        yosh = calculate_age(bd, today)
        k = days_until_birthday(bd, today)
        if k == 0:
            print(f"{name}: {yosh} yosh. Bugun tug'ilgan kun!")
        else:
            print(f"{name}: {yosh} yosh, keyingi tug'ilgan kunigacha {k} kun qoldi.")

report(members, date.today())
report(members, date(2026, 10, 13))