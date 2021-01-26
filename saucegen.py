#SUKA BLYAT HENTAI NHENTAI SAUCEEDO ED CODE SGENERATOERRER BY JL
#made by JL (and google searching)
import requests #used for HTTP requests
import os #used to open googrel chroem from bash
from random import randint #maek random nubmers
from bs4 import BeautifulSoup #for getting page content
from time import sleep

#globals
broadSearchPref = -1

print('Script by JL!')
#generate a random sauce code
print('NOTE: there is a 1 second delay between attempts in order to avoid spamming nhentai.net!\nMax 20 attempts to find a random sauce.')
for attempt in range(20): #repeate the following code 20 times
    sleep(1.00) #pause for one second to avoid spamming nhentai.net
    print(f'\nATTEMPT #{attempt + 1}...')
    print('Generating random code...')
    randomNumber = randint(100000, 999999) # generate our 6 digit random sos cod

    #check if the stuff exists
    print(f'testing if #{randomNumber} exists...')
    request = requests.head(f'https://nhentai.net/g/{randomNumber}/')
    print(f'Status code for header requests is {request.status_code}!')
    if request.status_code == 200: #status code 200 means success
        validURL = f'https://nhentai.net/g/{randomNumber}/'

        print('\a') #bell character
        print(f'#{randomNumber} exists!!! Go to {validURL}/') #boom is good

        pageData = requests.get(validURL) #get the page data
        print(f'Status code for data request is {pageData.status_code}!')
        if pageData.status_code != 200:
            print('Error connecting! Skip.')
            continue
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

        #Read the blacklist and the whitelist file
        checkBlackList = True
        checkWhiteList = False #feature disabled for now; unusable
        try:
            blacklistFile = open('blacklist.txt', 'r')
        except FileNotFoundError:
            checkBlackList = False
        try:
            whitelistFile = open('whitelist.txt', 'r')  
        except FileNotFoundError:
            checkWhiteList = False

        if checkBlackList:
            blacklistFile = open('blacklist.txt', 'r')
            blacklisted = blacklistFile.readlines()
            #scan the tags for blacklisted entries
            clearOfBadTags = True
            for i in tag:
                for b in blacklisted:
                    #skip comments
                    if b.startswith("#"):
                        continue
                    if i == b.strip():
                        clearOfBadTags = False
                        break
                if not clearOfBadTags:
                    break;

            if not clearOfBadTags:
                print('\nDoujin has blacklisted tags! Skipping...')
                continue

        if checkWhiteList:
            broadSearch = False
            if broadSearchPref == -1:
                print('\nNote: whitelists greately narrow down the accepted sauces and wastes time,')
                print('would you like to use broad searching?\n(The sauce will be accepted if there is ATLEAST ONE tag.)')
                uInput = input('[Yy/ENTER]: ')
                if uInput == 'Y' or uInput == 'y':
                    broadSearch = True
                    broadSearchPref = 1
                else:
                    broadSearchPref = 0
            else:
                broadSearch = True if broadSearchPref == 1 else False

            whitelistFile = open('whitelist.txt', 'r')
            whitelisted = whitelistFile.readlines()
            #scan the tags for blacklisted entries
            passesTagRequirements = True
            if not broadSearch:
                for w in whitelisted:
                    found = False
                    for i in tag:
                        #skip comments
                        if w.startswith("#"):
                            continue
                        if w.strip() == i:
                            found = True
                            break
                    if not found:
                        passesTagRequirements = False
                        break
            else:
                passesTagRequirements = False
                for w in whitelisted:
                    for i in tag:
                        #skip comments
                        if w.startswith("#"):
                            continue
                        if w.strip() == i:
                            passesTagRequirements = True
                            break
                        if passesTagRequirements:
                            break

            if not passesTagRequirements:
                print('\nDoujin does not contain the required whitelist tags! Skipping...')
                continue

        #give the user a heads up
        shouldOpenBrowser = True
        shouldAddToList = True
        uInput = input('\nPress ENTER to continue, F to only append to the sauce list, B to only open on browser,\n Q to exit, or R to retry...\n[ENTER/Ff/Bb/Qq/Rr]: ') 
        if uInput == 'Q' or uInput == 'q': #quit if the user entered Q (or q)
            quit()
        elif uInput == 'R' or uInput == 'r':
            attempt = 0 #uhh dosent actually do anything imma fix it later
            continue

        if uInput == 'F' or uInput == 'f':
            shouldOpenBrowser = False
        elif uInput == 'B' or uInput == 'b':
            shouldAddToList = False

        if shouldAddToList:
            with open('foundCodes.txt', 'a') as sauceList:
                print(f'Appending \"{randomNumber}\\n\" to foundCodes.txt...')
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
