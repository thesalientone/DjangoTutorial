from django import template

register = template.Library()

def sortVote(value):

    choice_votes = []
    for choice in value:
        choice_votes.append((choice.votes, choice))

    return sorted(choice_votes, key=first, reverse=True)

def first(a):
    return a[0]

def same_thing(value):
    return value

register.filter('sortVote', sortVote)
register.filter('same_thing', same_thing)



