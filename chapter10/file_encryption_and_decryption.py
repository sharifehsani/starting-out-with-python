"""
- Author: Sharif Ehsani
- Date: December 2020
- https://github.com/sharifehsani

Programming Exercises
3. File Encryption and Decryption
Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For
example:
codes = { 'A' : '%', 'a' : '9', 'B' : '@', 'b' : '#', etc...}
Using this example, the letter A would be assigned the symbol %, the letter a would be
assigned the number 9, the letter B would be assigned the symbol @, and so forth.
The program should open a specified text file, read its contents, and then use the dictionary
to write an encrypted version of the file’s contents to a second file. Each character in
the second file should contain the code for the corresponding character in the first file.
Write a second program that opens an encrypted file and displays its decrypted contents on
the screen.
"""

# main function to start the program
def main():

	# declare a dictionary variable and assign values for the alphabet keys
	codes = {
				'A': '%', 'a':'9', 'B': '@', 'b': '&', 'C':'$', 'c':'!', 'D':'^', 'd':'*', 'E':'<', 'e':'~',
				'F':'0', 'f':'+', 'G':'8', 'g':'=', 'H':'?', 'h':'L', 'I':'"', 'i':'1', 'J':';', 'j':'}',
				'K':'2', 'k':'t', 'L':'-', 'l':'z', 'M':'6', 'm':'|', 'N':'3', 'n':'#', 'O':'b', 'o':'4',
				'P':'5', 'p':'a', 'Q':'7', 'q':'g', 'R':'5', 'r':'h', 'S':'p', 's':'c', 'T':'j',
				't':'s', 'U':'n', 'u':'.', 'V':'R', 'v':'o', 'W':'x', 'w':')', 'X':'>', 'x':',',
				'Y':'k', 'y':'w', 'Z':'q', 'z':'(', ' ': '_', '\n': '/', '—': '—'
			}

	encrypt_text = ''
	
	# open the text file called encyrption_and_decryption.txt
	file_in = open('text_to_be_encrypted.txt', 'r')
	#line = file_in.readline()
	
	# loop through the original text in the txt file and match each character with the 
	# key in the dictionary if it matches wirte the value associated to the key to the
	# second file and close the file. Display the original text as well
	print()
	print('..............Original text.....................')
	for line in file_in:
		print(line,end='')
		for ch in line:
			for key in codes:
				if (ch == key):
					new_ch = codes[key]
					encrypt_text = encrypt_text + new_ch
		#line = file_in.readline()
	# close the file
	file_in.close()

	# display the encrypted text
	print()
	print('.................Encrypted text...................')
	print(encrypt_text)

	# open a text file for writting the encrypted text to, write the te
	file_out = open('encrypted_text.txt', 'w')
	file_out.write(encrypt_text)
	# close the file
	file_out.close()

	# lets decrypte the file back
	# open the encrypted file
	decrypt_text = ''
	file_in_2 = open('encrypted_text.txt', 'r')

	# iterate through the file and match the character in the file with value of in dictonary
	# if matched write the key to decrypted text
	for line in file_in_2:
		for ch in line:
			for key in codes:
				if (ch == codes[key]):
					decrypt_text = decrypt_text + key

	# display the decrypted text
	print()
	print('..............Decrypted text......................')
	print(decrypt_text)

# call the main function
main()
