** IMPORTANT : IF YOU ARE JUST GOING TO COPY AND PASTE DONT BE A DUMBASS AND JUST SUBMIT WHAT YOU COPIED, CHANGE THE VARIABLE NAMES, CHANGE THE PLACE WHERE THE FUNCTION ARE CREATED, DECLARE THE FUNCTIONS DIFFERENTLY... DON"T BE THAT DUMB**


Implementation Details




Step 1 – Implementing the welcome() function (10%):



To implement this function, you simply need to print an introduction to the user. You should use the following message:

Welcome to the Caesar Cipher


This program encrypts and decrypts text with the Caesar Cipher.




Step 2 – Implementing the enter_message() function(15%):



To implement this function, you need to request input from the user to determine the mode of conversion and the message that they would like to encrypt or decrypt.


Your function should check if the mode the user entered is valid. If not, it should continue to prompt the user until a valid mode is selected.


The function should return two strings, the mode of conversation and the message. The message should be converted to upper case to avoid potential encrypting/decrypting issues.


Example Implementation:


>>> enter_message()
```
Would you like to encrypt (e) or decrypt (d): g

Invalid Mode

Would you like to encrypt (e) or decrypt (d): e

What message would you like to encrypt: Hello WORld

What is the shift number: a

Invalid Shift

What is the shift number: 4

('e', 'HELLO WORLD',4)
```



Step 3 – Implementing the encrypt() function (25%):



To implement this function, you need to correctly encrypt a plain text message as encrypted text. It should take 2 parameters, the message to be encrypted, and the shift number.


Your function should return a single value, a string - the encrypted message.


Example Implementation:

```
 encrypt("Hello World", 4)
'LIPPS ASVPH'
```



Step 4 – Implementing the decrypt() function(25%):



To implement this function, you need to correctly decrypt a message as decrypted text. It should take 2 parameters, the message to be decrypted, and the shift number.


Your function should return a single value, a plain text string.

Implementation:

```
 decrypt('LIPPS ASVPH',4)
'HELLO WORLD'
```


File Input/Output (25%):


The Caesar Cipher that you’ve developed can only encrypt or decrypt a single message at a time. Therefore, your task for this task will be to attempt to resolve this issue by implementing file reading/writing capabilities so that multiple messages can be encrypted/decrypted in one go.


To do this, you will need to implement the process_file(),write_messages(), is_file() and message_or_file() functions.


The first function process_file() should take two parameters, the filename from which messages should be read and the mode of operation (encrypting/decrypting). It should process the lines in the file one by one, returning a list of encrypted/decrypted messages.


A file has been added to the assessment page on Canvas, messages.txt, that includes a series of plain text strings, which you can use to test your function.


Implementation:

```
 process_file('messages.txt', 'e')
```


The second function is_file() should take a single parameter, a filename and return a Boolean value (True/False) depending upon whether the file exists within the current folder. There are several ways that you can achieve this, for example using exception handling logic or through the built-in OS module included with Python.


Implementation:

```
is_file('messages.txt')

True
```

The third function write_messages() should take a single parameter, a list of strings. It should write these strings to a file called results.txt, with each item taking up a single line.


The function doesn’t need to return anything.



The fourth function message_or_file() should work similarly to the enter_message() function you developed earlier. It shouldn’t take any parameters, but needs to return three values, the mode ("e" or "d" based on whether the user would like to encrypt or decrypt), a message if the user would like to process messages using the console (or None) and a filename if the user would like to process data in a file (or None). You should continue to validate the mode that the user enters as well as the input mechanism (file/console).


In addition, you should call your is_file() function to verify filenames. Users should be repeatedly prompted to enter the filename if the file doesn’t exist.


Example Implementation:

```
 message_or_file()
```

```
Would you like to encrypt (e) or decrypt (d):g

Invalid Mode

Would you like to encrypt (e) or decrypt (d):e

Would you like to read from a file (f) or the console (c)? f

Enter a filename: something_silly.txt

Invalid Filename

Enter a filename: messages.txt

What is the shift number: 4

('e', None, 'messages.txt')

```

```
 message_or_file()
```

```
Would you like to encrypt (e) or decrypt (d): g

Invalid Mode

Would you like to encrypt (e) or decrypt (d): e

Would you like to read from a file (f) or the console (c)? c

What message would you like to encrypt: Hello WORld


('e', 'HELLO WORLD', None)
```



You will also need to update your main() function to call the functions you’ve implemented.




Full Implementation (user input in red)

```
Welcome to the Caesar Cipher

This program encrypts and decrypts text using Caesar Cipher.

Would you like to encrypt (e) or decrypt (d): d

Would you like to read from a file (f) or the console (c)? c

What message would you like to decrypt: LIPPS ASVPH

What is the shift number: 4

HELLO WORLD

Would you like to encrypt or decrypt another message? (y/n): y

Would you like to encrypt (e) or decrypt (d): e

Would you like to read from a file (f) or the console (c)? c

What message would you like to encrypt: Hello WORld

What is the shift number: 4

LIPPS ASVPH

Would you like to encrypt or decrypt another message? (y/n): y

Would you like to encrypt (e) or decrypt (d): e

Would you like to read from a file (f) or the console (c)? f

Enter a filename: something_silly.txt
```
