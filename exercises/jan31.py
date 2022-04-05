message = "Good Morning 2"
names_list = ['Ed', 'Alex', 'Tom', 'Kim']
names_tuple = ('Ed', 'Alex', 'Tom', 'Kim')


def say_good_morning(message1, name="Jordan"):  # parameter
    print(message1, name)


names_list[0] = 'Maria'


for name in names_list:
    say_good_morning(message, name)
# sayGoodMorning camelCase


# say_good_morning sneak_case
