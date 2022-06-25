#   Playing with Regex

import re

phoneCheck = 'I called the number given to me: 07912 654 321 and it did not ring, even once. So I tried 0800 090 0123 instead'
emailCheck = 'Last thing I did was send an email to tester@tester21.co.uk this morning'

phoneR1 = r'(\d{5} \d{3} \d{3})|(\d{4} \d{3} \d{4})'
emailR1 = r'(\w+)@(\w+)[.](\w*)([.]\w*)?'

regs = re.compile(phoneR1);

#   Phone number regex

mob = regs.search(phoneCheck);

print('Mobile number found: ' + mob.group())

#   STRIP text of all punction

stripExpr = r'[^A-z0-9 ]';
stripReg = re.compile(stripExpr);

chat = "What's up with you guys, you're acting really weird?"

res = stripReg.sub('', chat).lower();
print (res)
