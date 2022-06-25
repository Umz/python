#   MAGIC 8 Ball

import random

messages = ['It is certain',
            'Decidely so',
            'Yes, Definitely',
            'Hazy.... Try again later',
            'Ask again later!',
            'Concentrate and ask again',
            'My reply is no!',
            'Outlook, not so good',
            'Very doubtful']

print ('What do you want?')
qs = input()

print(messages[random.randint(0, len(messages) - 1)])
