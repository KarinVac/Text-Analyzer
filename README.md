TEXT ANALYZER
```


credentials.py
task_template.py


A program that can process any text of arbitrary length and extract various information from it.

1. The program will request the user's username and password.
2. It will check whether the entered credentials match any of the registered users.
3. If the user is registered, it will greet them and allow them to analyze texts.
4. If the user is not registered, it will alert them and terminate the program.


5. The program will let the user choose from three texts stored in the TEXTS variable:
    - If the user selects a text number that is not in the range, the program will alert them and exit. 
    - If the user enters anything other than a number, the program will also alert them and exit.


6. For the selected text, the program will calculate the following statistics:
    - number of words
    - number of words starting with a capital letter
    - number of words written in uppercase
    - number of words written in lowercase
    - number of numbers (not digits)
    - sum of all numbers (not digits) in the text

5. The program will display a simple bar chart representing the frequency of different word lengths in the text. For example:

  7| * 1
  8| *********** 11
  9| *************** 15
 10| ********* 9
 11| ********** 10

After running the program, it should proceed as follows:

$ python projekt1.py
username:bob
password:123
----------------------------------------
Welcome to the app, bob
We have 3 texts to be analyzed.
----------------------------------------
Enter a number btw. 1 and 3 to select: 1
----------------------------------------
There are 54 words in the selected text.
There are 12 titlecase words.
There are 1 uppercase words.
There are 38 lowercase words.
There are 3 numeric strings.
The sum of all the numbers 8510
----------------------------------------
LEN|  OCCURENCES  |NR.
----------------------------------------
  1|*             |1
  2|*********     |9
  3|******        |6
  4|***********   |11
  5|************  |12
  6|***           |3
  7|****          |4
  8|*****         |5
  9|*             |1
 10|*             |1
 11|*             |1

If the user is not registered:

$ python project1.py username:marek password:123```
Unregistered user, terminating the program...
