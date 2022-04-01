# Tweepy - Twitter API Project

 Jonathan Moran
 
 University of Dayton, CPS 470 Computer Networks and Security
 
 Dr. Zhongmei Yao

---

NOTICE: 

--The Python version I used to test my code was Python 3.10

--TWEEPY MUST BE INSTALLED in order to run any python script

---

Tasks123.py :

	To compile/run my source code do the following:
		users = api.lookup_users(screen_name={"AnnieWesner", "swavey_jake"})
		^^ the line of code above can have different screen_names as elements for testing different results for task 1 and task 2
		^^ the line of code above was useful for testing the mutual friends part of task 2 (they had recent followers of count=20 that they also followed back)

	you can also change the values for the "count" variable and "newCount" variable to change the number of results given
		"count" --> represents the number of followers print and looped through for a particular users	
		"newCount" --> represents the number of tweets printed and looped through for the given values of task 3.a and 3.b

	(note: for the mutual friends part of Task 2, I have it only check the latest count=20 followers to save run time and not overload the rate limit of tweepy)



Task4.py :

	To compile/run my source code do the following:
		run the program
		type in a name
		type in the number of tweets you would like to receive in the email
		type in keywords you want to be included in the tweets you receive
		type in the email address that you want to receive the email
	(the program instantly sends you email based on the keywords you provide it)
	(run the program and read the printed code for instructions and sample code that could be inputted)
	
# SEE 'CPS470-Assignment2Complete-JonathanMoran.pdf' FOR SAMPLE RUN/OUTPUT
