import unicodecsv

with open('/Users/anujjha/Documents/DataAnalysis/Udacity/enrollments.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)

print enrollments[0]

with open('/Users/anujjha/Documents/DataAnalysis/Udacity/daily_engagement.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)

print "daily engagement"
print enrollments[0]

def ref():list
  
