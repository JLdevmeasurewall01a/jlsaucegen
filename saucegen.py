#SUKA BLYAT HENTAI NHENTAI SAUCEEDO ED CODE SGENERATOERRER BY JL
#made by JL (and google searching)
import requests #used for HTTP requests
import os #used to open googrel chroem from bash
from random import randint #maek random nubmers
from bs4 import BeautifulSoup #for getting page content
#FUTURE PLANS: have a blacklist so that it will not give the user sauce that has tags they dont like
#this assumes you use google chrome!

#generate a random sauce code
print('Max 5 attempts to find a random sauce.')
for attempt in range(5): #repeate the following code 5 times
	print(f'\nATTEMPT #{attempt + 1}...')
	print('Generating random code...')
	randomNumber = randint(100000, 999999) # generate our 6 digit random sos cod

	#check if the stuff exists
	print(f'testing if #{randomNumber} exists...')
	request = requests.head(f'https://nhentai.net/g/{randomNumber}/')
	if request.status_code == 200: #status code 200 means success
		validURL = f'https://nhentai.net/g/{randomNumber}/'
		
		print('\a') #bell character
		print(f'#{randomNumber} exists!!! Go to {validURL}/') #boom is good
		
		pageData = requests.get(validURL) #get the page data
		soup = BeautifulSoup(pageData.text, 'html.parser')
		tags = soup.find_all('span', class_='name')
		tag = [i.text for i in tags]
		
		print('Tags : ', end = '')
		tLoopAmnt = 0
		for i in tag:
			print(i+', ', end = '')
			if tLoopAmnt > 3:
				print(' ')
				tLoopAmnt = 0
			tLoopAmnt = tLoopAmnt + 1
			
		
		#give the user a heads up
		shouldOpenBrowser = True
		shouldAddToList = True
		uInput = input('\nPress ENTER to continue, F to only append to the sauce list, B to only open on browser,\n Q to exit, or R to retry...\n') 
		if uInput == 'Q' or uInput == 'q': #quit if the user entered Q (or q)
			quit()
		elif uInput == 'R' or uInput == 'r':
			attempt = 0
			continue
		
		if uInput == 'F' or uInput == 'f':
			shouldOpenBrowser = False
		elif uInput == 'B' or uInput == 'b':
			shouldAddToList = False
			
		if shouldAddToList:
			with open('foundCodes.txt', 'a') as sauceList:
				sauceList.write(f'{randomNumber}\n') #add this code to our S A U C E list!
		if shouldOpenBrowser:
			print('Google chrome:')
			os.system(f'google-chrome --incognito {validURL}') #open chrome!
			print('====================')
		
		print('OK is good!\ngoodbye you horny fuck\n')
		quit();
	else:
		print('Try again. not exist >:(') #oof try again
		
print('\n\naw!\ntry again you stupid horny fuck!\n')
