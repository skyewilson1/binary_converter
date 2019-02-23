def convert(optional):
	i = ""
	for x in optional: 
		i += x
	return i 
print "Don't be a dick! This converter will change all letters into uppercase only, it also does not recognize symbols and signs."
binlist = {"A" : "01000001", "B" : "01000010", "C" : "01000011", "D" : "01000100", "E" : "01000101", "F" : "01000110", "G" : "01000111", "H" : "01001000", "I" : "01001001", "J" : "01001010", "K" : "01001011", "L" : "01001100", "M" : "01001101", "N" : "01001110", "O" : "01001111", "P" : "01010000", "Q" : "01010001", "R" : "01010010", "S" : "01010011", "T" : "01010100", "U" : "01010101", "V" : "01010110", "W" : "01010111", "X" : "01011000", "Y" : "01011001", "Z" : "01011010", " " : "00100000"}
usermessage = raw_input("enter message here: ")
useroutput = []
print2user = convert(useroutput)
userlist = list(usermessage)
for x in userlist:
	if x in binlist: useroutput.append(binlist[x])				
	else: print "character not found"


