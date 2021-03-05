'''                 Dictionaries

'''
my_dictionary = {'name':'rich', 'course': 'python', 'fav_food': 'ice cream'}

phone_dict = {'rich': '555-55-5555',
             'roger': '999-99-0000',
             'joe_blow': 'fail-o-so-bad'}
print(my_dictionary)  # {'name': 'rich', 'course': 'python', 'fav_food': 'ice cream'}


word_dict = {
            'a':
                {
                'apple': 'the round fruit of a tree of the rose family',
                'ant': 'an insect which cleans up the floor'
                },
            'b':
                {
                'bad': 'of poor quality or low standard',
                'business': 'season 8 of GOT'
                }
            }
print(word_dict)  # {'a': {'apple': 'the round fruit of a tree of the rose family', 'ant': 'an insect which cleans up the floor'}, 'b': {'bad': 'of poor quality or low standard', 'business': 'season 8 of GOT'}}

print(word_dict['a'])  # {'apple': 'the round fruit of a tree of the rose family', 'ant': 'an insect which cleans up the floor'}

print(word_dict['b'])  # {'bad': 'of poor quality or low standard', 'business': 'season 8 of GOT'}

print(word_dict['b']['business'])  # {'bad': 'of poor quality or low standard', 'business': 'season 8 of GOT'}

print(word_dict['b']['business'])
