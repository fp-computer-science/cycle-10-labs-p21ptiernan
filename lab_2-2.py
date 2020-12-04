# Author PT 12/4/20

def email(lst):
    for name in lst:
        print("Hi {0}, you're invited to my birthday party on Friday!".format(name))


email(['John', 'Jane', 'Jack'])
