# Jeremiah Gallagher
# CSIS-354
# Consuming Web Services with Python

# ProcessAPI.py

#  " Scripture quoted by permission. All scripture quotations, unless otherwise indicated, are taken
#  from the NET Bible® copyright ©1996-2018 by Biblical Studies Press, L.L.C. All rights reserved."

import requests


# ask the user to choose what type of verse they want to view, and then assign their choice to the variable that will
# be attached to the http request.
def getPassage():
    user_choice = 0                               # define user_choice
    while user_choice < 1 or user_choice > 3:     # loop until the user makes a valid decision
        print('1)  Verse of the day.')
        print('2) Random verse.')
        print('3) Verse of your choice.')
        print('4) Exit Program')
        user_choice = int(input("What is your selection?"))    # capture user's choice
        if user_choice == 1:
            user_passage = 'votd'
        elif user_choice == 2:
            user_passage = 'random'
        elif user_choice == 3:
            user_book = input('Please enter the name of the book:')        # capture book name
            user_chapter = input('Please enter the chapter')               # capture chapter
            user_verses = input('Please enter the verse or verses, "example: 1 or 1-3"')   # capture verse/s
            user_passage = user_book + " " + user_chapter + ":" + user_verses   # build a string from inputs
        elif user_choice == 4:
            print("Thank you for using the verse retriever.  Have a nice day!")    # option to exit
            exit(0)
        else:
            print('That is not a valid choice')                     # any input outside of choice range prints this
    return user_passage                                             # return the choice to main


def main():
    print("Welcome to the Bible.org verse retriever." + '\n' + 'Please make a selection:' + '\n')

    decision = True                         # decision defined as true
    while decision:                         # and used to loop main until user is done
        user_passage = getPassage()         # get the user's choice
        payload = {'passage': user_passage, 'type': 'json'}  # assign params to a variable

        my_request = requests.get('http://labs.bible.org/api/?', params=payload)  # build the api request results string

        my_dict = my_request.json()  # create a list from the request

        new_dict = dict(my_dict[0])  # build a dictionary from the list
        print('\n' * 3)  # add spacing for easier reading
        print(new_dict['bookname'] + ' ' + new_dict['chapter'] + ':' + new_dict['verse'] + ' reads: ')  # print results
        print(new_dict['text'])   # print text of results

        unanswered = True  # used to loop inner while loop until user makes a decision
        print('\n' * 2)   # add spacing for easier reading
        print("Do you want to look up another verse?")
        while unanswered:
            user_answer = input('press Y or N')
            print('\n' * 3)   # add spacing for easier reading
            if user_answer == 'Y' or user_answer == 'y':  # allow for upper and lowercase input
                decision = True
                unanswered = False
            elif user_answer == 'N' or user_answer == 'n':  # allow for upper and lowercase input
                decision = False
                unanswered = False
            else:
                unanswered = True
                print('Please make a valid selection')

    print("Thank you for using the verse retriever.  Have a nice day!")  # exit the program
    return 0


main()
