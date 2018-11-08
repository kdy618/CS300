'''
Eliza300: Postconditions
1. (Welcome): A welcome message is on the console
2. (Complaint): A complaint was entered by the user in response to a prompt
3. (Duration): A duration in months was entered by user in response to a prompt
4. (Error check): EITHER the user entered an integer between 1 and 100 for duration 
	after being given up to two chances OR the application quit after suggesting a re-run.
5. (Action Recommended): EITHER how_long exceeds 2 months, and the phrase
   “ … months is too much time to go without help! Let's schedule a few 
   sessions" is on the console OR the following is on the console:
   "Come back in a couple of months if this persists".
'''

intro = 'Thank you for using Eliza300, a fun therapy program.'
print(intro)
complaint = input('Please state your complaint: ')
monthsOfExp = input('How many months has it been that you have experienced ' + "'{}'".format(complaint) + '? ')

if monthsOfExp.isdigit(): 
	if int(monthsOfExp) >= 1 and int(monthsOfExp) <= 100: 
		if int(monthsOfExp) > 2: 
			print(monthsOfExp + ' ' + "months is too much to go without help! Let's schedule a few sessions.")
		else: 
			print('Come back in a couple of months if this persists.')
	else:
		print('You must enter the duration in months between 1 and 100.')
else: 
	retryMonthsOfExp = input('Please try one more time to enter duration in months less than 100: ')
	if retryMonthsOfExp.isdigit():
		if int(retryMonthsOfExp) >= 1 and int(retryMonthsOfExp) <= 100: 
			if int(retryMonthsOfExp) > 2: 
				print(retryMonthsOfExp + ' ' + "months is too much to go without help! Let's schedule a few sessions.")
			else: 
				print('Come back in a couple of months if this persists.')
	else:
		import sys
		sys.exit()
 


