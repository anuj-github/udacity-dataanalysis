import unicodecsv
import Parser
import pprint


def parse(file_name):
    with open(file_name, 'rb') as files:
        reader = unicodecsv.DictReader(files)
        return list(reader)


# parse enrollment data
enrollments = parse('/Users/anujjha/Documents/DataAnalysis/Udacity/enrollments.csv')
for enrolment in enrollments:
    enrolment['cancel_date'] = Parser.parse_date(enrolment['cancel_date'])
    enrolment['days_to_cancel'] = Parser.parse_Int(enrolment['days_to_cancel'])
    enrolment['account_key'] = Parser.parse_Int(enrolment['account_key'])
    enrolment['is_udacity'] = enrolment['is_udacity'] == 'True'
    enrolment['is_canceled'] = enrolment['is_canceled'] == 'True'
    enrolment['join_date'] = Parser.parse_date(enrolment['join_date'])
print 'enrolments'
pprint.pprint(enrollments[0])

# parse daily engagement data
daily_enagements = parse('/Users/anujjha/Documents/DataAnalysis/Udacity/daily_engagement.csv')
for daily_enagement in daily_enagements:
    daily_enagement['acct'] = Parser.parse_Int(daily_enagement['acct'])
    daily_enagement['lessons_completed'] = Parser.float_to_int(daily_enagement['lessons_completed'])
    daily_enagement['num_courses_visited'] = Parser.float_to_int(daily_enagement['num_courses_visited'])
    daily_enagement['projects_completed'] = Parser.float_to_int(daily_enagement['projects_completed'])
    daily_enagement['total_minutes_visited'] = Parser.float_to_int(daily_enagement['total_minutes_visited'])
    daily_enagement['utc_date'] = Parser.parse_date(daily_enagement['utc_date'])

print 'daily_enagement'
pprint.pprint(daily_enagements[0])

# parse project submissions data
project_submissions = parse('/Users/anujjha/Documents/DataAnalysis/Udacity/project_submissions.csv')
for project in project_submissions:
    project['account_key'] = Parser.parse_Int(project['account_key'])
    project['lesson_key'] = Parser.parse_Int(project['lesson_key'])
    project['creation_date'] = Parser.parse_date(project['creation_date'])
    project['completion_date'] = Parser.parse_date(project['completion_date'])

print 'projects'
pprint.pprint(project_submissions[0])
