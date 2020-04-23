"""
Name: Yunlu Li
Userid: yl4df

Pledge: I do not receive or give any unauthorized aid during the exam.
"""
from __future__ import print_function # make python2 print like python3

"""
Complete this function so that it
returns the attendee who is the superstar.

Input is a list of attendees at the conference.
The return type is the same as items in the list, so you should return 
   one of the values stored in the list of attendees.

You must use the knows() function below
to check who knows whom.
"""
def findSuperstar(attendees):
    # Base Case:
    if (len(attendees)==1):
        return attendees[0]
    candidate_list=[]
    if (len(attendees)%2==0):
        for i in range(0,len(attendees)//2):
            a_knows_b = knows(attendees[i], attendees[len(attendees)//2+i])
            b_knows_a = knows(attendees[len(attendees)//2+i], attendees[i])
            if ( a_knows_b and not b_knows_a):
                candidate_list.append(attendees[len(attendees)//2+i])
            if (not a_knows_b and b_knows_a):
                candidate_list.append(attendees[i])
    if (len(attendees)%2!=0):
        for i in range(0, (len(attendees)-1)//2):
            c_knows_d = knows(attendees[i], attendees[(len(attendees)-1)//2+i])
            d_knows_c = knows(attendees[(len(attendees)-1)//2+i], attendees[i])
            if ( c_knows_d and not d_knows_c):
                candidate_list.append(attendees[(len(attendees)-1)//2+i])
            if (not c_knows_d and d_knows_c):
                candidate_list.append(attendees[i])
            candidate_list.append(attendees[len(attendees)-1])
    return findSuperstar(candidate_list)


#####################################
# Under penalty of the Honor Code   #
# Do Not Change Anything Below Here #
# (In your final submission)        #
#####################################


def knows(attendee_a, attendee_b):
    """
    returns true if attendee_a knows attendee_b
    """
    global knows_calls_counter
    knows_calls_counter += 1
    return attendee_b in who_knows_whom[attendee_a]


#########################################
# Under penalty of the Honor Code       #
# Do not use anything initialized below #
# (In your final submission)            #
#########################################


knows_calls_counter = 0
conference_file = open("conference2.txt", 'r')
who_knows_whom = {}
attendee_list_given = []
for line in conference_file.readlines():
    if len(line.strip()) == 0:
        continue
    line_list = line.split()
    person_at_conference = line_list[0]
    known_by_person = line_list[1:]
    who_knows_whom[person_at_conference] = known_by_person
    attendee_list_given.append(person_at_conference)

# Call the findSuperstar function, print the result and the number of times you called knows
print(findSuperstar(attendee_list_given), knows_calls_counter)
