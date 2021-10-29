'''My solution'''


def title_case(title, minor_words=''):
    if title == '':
        return ''
    new_title = []
    new_title.append(title.split()[0].capitalize())
    for word in title.lower().split()[1:]:
        if word in minor_words.lower().split():
            new_title.append('{}'.format(word))
        else:
            new_title.append('{}'.format(word.capitalize()))
    return ' '.join(new_title)
        
print(title_case('', '')) #Result: ''
print(title_case('a clash of KINGS', 'a an the of')) #Result: A Clash of Kings
print(title_case('THE WIND IN THE WILLOWS', 'The In')) #Result: The Wind in the Willows
print(title_case('the quick brown fox')) #Result: The Quick Brown Fox

'''
    Best Practices:


        def title_case(title, minor_words=''):
            title = title.capitalize().split()
            minor_words = minor_words.lower().split()
            return ' '.join([word if word in minor_words else word.capitalize() for word in title])

'''