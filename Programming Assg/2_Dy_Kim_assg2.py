
'''
Eliza300: Postconditions
1. (Welcome): A welcome message is on the console
2. (Complaint): A complaint was entered by the user in response to a prompt
3. (Duration): A duration was entered by user in response to a prompt
4. (Action Recommended): EITHER how long exceeds 2 months, and the phrase
   “ … months is too much time to go without help! Let's schedule a few sessions"
   is on the console
   OR the following is on the console:
   "Come back in a couple of months if this persists".
'''

intro = 'Thank you for using Eliza300, a fun therapy program.'
print(intro)
complaint = input('Please state your complaint: ')
respone = "How many months has it been that you have experienced '{}'? "
monthsOfExp = input(respone.format(complaint))
confirm = "{}  months is too much to go without help!"
    " Let's schedule a few sessions."

if monthsOfExp.isdigit():
    if int(monthsOfExp) > 2:
        print(confirm.format(monthsOfExp))
    else:
        print('Come back in a couple of months if this persists.')
