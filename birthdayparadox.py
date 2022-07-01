"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, math, simulation"""

import datetime, random

def getBirthdays(numberofBirthdays):
    birthdays = []
    for i in range(numberofBirthdays):
        # year is unimportant, as long as all birthdays have same year
        startofYear = datetime.date(2001, 1, 1)
        randomNumberofDays = datetime.timedelta(random.randint(0, 364))
        birthday = startofYear + randomNumberofDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    # compare each birthday to every other birthday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1 :]):
            if birthdayA == birthdayB:
                return birthdayA

def main():
    MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

    while True:
        print('How many birthdays shall I generate? (Max 100)')
        response = input('> ')
        if response.isdecimal() and (0 < int(response)):
            numBDays = int(response)
            break
    print()

    print('Here are', numBDays, 'birthdays:')
    birthdays = getBirthdays(numBDays)
    for i, birthday in enumerate(birthdays):
        if i != 0:
            print(',', end='')
            monthName = MONTHS[birthday.month -1]
            dateText = '{} {}'.format(monthName, birthday.day)
            print(dateText, end='')
    print()
    print()

    match = getMatch(birthdays)

    print('In this simulation, ', end='')
    if match != None:
        monthName = MONTHS[match.month - 1]
        dateText = '{} {}'.format(monthName, match.day)
        print('multiple people have a birthday on', dateText)
    else:
        print('there are no matching birthdays.')
    print()

if __name__ == '__main__':
    main()
