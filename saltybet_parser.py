#! /usr/bin/env python2

# Arsh Chauhan
# 09/12/2016
# saltybet_parser.py: Read a chat log of the salty bet twitch chat and return macthes and winners
# Based on chat logger created by Mike Moss (https://github.com/mrmoss/saltybet_tracker) 

#TO DO: Parse data into a DB to be able to run analytics

def parseSalty(fileName):
	logFile = open(fileName,'r')
	for line in logFile:
		betsOpen = line.find('Bets are OPEN for') #Bot posts this message when bets open 
		if betsOpen != -1:
			betsOpen = betsOpen+len('Bets are OPEN for')
			playerOneNameStart = betsOpen
			vsIndex = line.find('vs') #player names separatd by 'vs'
			playerTwoEndStart = line.find('!')
			playerOneName = line[playerOneNameStart:vsIndex-1].strip()
			playerTwoName = line[vsIndex+2:playerTwoEndStart].strip()
			print("Player 1: "+ playerOneName) 
			print ("Player 2:" + playerTwoName)

		index = line.find('wins')
		if index != -1:
			exclamationIndex = line.find('!')
			if exclamationIndex != -1:
				print("Winner: " + line[:index-1])
				print('\n')

if __name__ == '__main__':
	parseSalty("salty_log")
