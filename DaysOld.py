# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
# Determine if this is a leap year
def isleap(year):
    if year % 4 !=0:
        return False
    if year % 100 !=0:
        return True
    if year % 400 !=0:
        return False
    return True
    
#print isleap(1900)
        
def daysinyear(year):
    if isleap(year):
        return 366
    return 365
    
#print daysinyear(2015)

def daysinmonth(year,month):
    if month==1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    else:
        if month==2:
            if isleap(year):
                return 29
            return 28
        return 30
        
#print daysinmonth(2016,3)

def cumdaysyr(year):
    n=1900
    days=0
    while n<year:
        days=days+daysinyear(n)
        n=n+1
    return days
    
#print cumdaysyr(2012)

def cumdaysmo(year,month):
    n=1
    days=0
    while n<month:
        days=days+daysinmonth(year,n)
        n=n+1
    return days
    
#print cumdaysmo(2012,2)

def daysBetweenDates (year1,month1,day1,year2,month2,day2):
    date1=cumdaysyr(year1)+cumdaysmo(year1,month1)+day1
    date2=cumdaysyr(year2)+cumdaysmo(year2,month2)+day2
    return date2-date1

#print daysBetweenDates (2012,2,1,2013,2,12)            
            

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                 ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
