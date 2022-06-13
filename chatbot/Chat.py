#   Chat.py bot for the bot to use what it has learnt to conversate and learn

import time, sys, re

#phrases = []       #   ALL phrases
#seqs = ['0.']          #   ALL sequences stored
sequence = ''

phrases = ['hello', 'hi', 'how are you', 'im good and you', 'fine thanks', 'busy today', 'yea busy', 'are you', 'very busy']
seqs = ['0.', '0.1.2.3.4.5.6.7.8.']


#   LOAD data from file

#   STRING CLEANING

stripExpr = r'[^A-z0-9 ]';
stripReg = re.compile(stripExpr);

#   INSTRUCTIONS

print('Chat Bot (SCB-V1-UG)')
print('Bot learns to chat by copying you')
print('SCB: *Learning Mode*')
print('SCB: Welcome to chat.')

#   CHATTING

while True:

    #   1- GET user input

    usr = input();
    print ('-')
    msg = stripReg.sub('', usr).lower()    #   CLEAN and normalise input

    if usr == 'exit':

        #   SAVE to file

        # if (new sequence, no match
        seqs.append(sequence)

        print(phrases)
        print(seqs)
        print(sequence)
        
        break

    elif msg in phrases:
        
        time.sleep(.5)
        index = phrases.index(msg)

        #   TRY index + 1 otherwise, (I don't know what to say next..)

        try:

            #   Rename here and - index is ID

            findSeq = sequence + '.' + str(index)

            #   SEARCH for this sequence match in array
            
            openSeq = findSeq.split('.')[-5:]
            search = '.'.join(openSeq)
            print(search)
            
            #   LOOP down from 5
            #   fn - return response index
            rSeq = '';
            for sq in seqs:
                if search in sq:
                    rSeq = sq
                    break

            memList = rSeq.split('.')
            memIndex = memList.index(str(index))
            respIndex = memList[memIndex + 1]
            
            #   end fn-
            
            response = phrases[int(respIndex)]
            print ('SCB: ' + response)

            #   add index of response to the sequence
            sequence += str(phrases.index(msg)) + '.'
            
        except:
            print ("SCB: How do I respond to this?")
            
        print ('-')

    #   ELSE new item, add to phrases and to sequence

    else:
        
        phrases.append(msg)
        sequence += str(phrases.index(msg)) + '.'

        print ('SCB: *Learned "' + usr + '"*\n');
        time.sleep(.5)
        print ('SCB: ' + msg)
        print ('-')

print ('SAVING and CLOSING')
