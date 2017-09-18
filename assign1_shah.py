import re
from datetime import datetime



class AverageCalc( object ):

    def average(num):

        avg = int(sum(num))/int(len(num))

        if  avg<6:
            print('Low average')

        elif avg>6 and avg<12:
            print('medium average')

        elif avg>12:
            print('High ave')

    @classmethod
    def decorator(cls, strng):
        int_list = [int(s) for s in re.findall('\d+', strng)]
        return (int_list)

    def article(str):
        dateFormat = "%d-%m-%Y"
        articlePattern = re.compile("(?<article>\w+)/(?<year>\w+)/(?<month>\w+)/(?<day>\w+)/(?<articleName>\w+)")
        result = articlePattern.match(str)

        datestr = result.group("day") + "-" + result.group("month") + "-" + result.group("year")
        today = datetime.now().strftime("%d-%m-%Y")

        olddays= datetime.strptime(datestr, dateFormat)
        newdays = datetime.strptime(today, dateFormat)

        print(result.group("name"), datestr, (newdays-olddays).days)


lowlist = [2, 4, 2, 1]
medlist = [6,8,6]
highlist = [8,12, 23]
findavg = AverageCalc.average(lowlist)
findavg = AverageCalc.average(medlist)
findavg = AverageCalc.average(highlist)


num = raw_input('Enter any numbers and letters: ')

print (AverageCalc.decorator(num))

articleDetails = AverageCalc.article("articles/2010/10/21/my_summer")


