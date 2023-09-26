from datetime import date
def check(month, year): 
    return str(date(year,month,13).strftime("%A")=='Friday')

print(check(4,2019))