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

print(word_dict['b']['business'])  # season 8 of GOT

print(word_dict['b']['business'], word_dict['b']['bad'])  # season 8 of GOT of poor quality or low standard

print(my_dictionary.get('name'))  # rich

print(my_dictionary.get('job'))  # None

my_dictionary['job'] = 'python programmer'
print(my_dictionary.get('job'))  # python programmer
print(my_dictionary)  # {'name': 'rich', 'course': 'python', 'fav_food': 'ice cream', 'job': 'python programmer'}


my_dictionary['course'] = 'java'
print(my_dictionary)  # {'name': 'rich', 'course': 'java', 'fav_food': 'ice cream', 'job': 'python programmer'}


print(my_dictionary.keys())  # dict_keys(['name', 'course', 'fav_food', 'job'])


print(my_dictionary.values())  # dict_values(['rich', 'java', 'ice cream', 'python programmer'])


print(my_dictionary.items())  # dict_items([('name', 'rich'), ('course', 'java'), ('fav_food', 'ice cream'), ('job', 'python programmer')])


for k,v in my_dictionary.items():
    print(k, v)  # name rich
                # course java
                # fav_food ice cream  ## this one shown in course video
                # job python programmer


