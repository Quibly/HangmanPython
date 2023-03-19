# Overview

I created a game of hangman using Python that I integrated with a Cloud Database (Firebase) to store puzzles and keep track of user data. The two work well together and the functionality of the program is nice. You'll be able to change user information in the menu when the program starts.

I wrote this software because I wanted to familiarize myself with Firebase. I'm familiar with Python and I wanted to work with a database that works well with it. I am impressed with Firebase because it keeps things simple. I found myself repeating commands a lot more than I expected. There wasn't a lot of guess work once I figured the basics out. 

[Software Demo Video](https://youtu.be/n666DA7kPVM)

# Cloud Database

I used a Firebase database. It is hosted through the Google Cloud Platform. I needed to get some credential certificates to authenticate my server first and then I needed to initialize the database with Firebase. Things got easier as I progressed in learning Firebase.

I created 2 tables that worked together a little bit. One table holds puzzles that can be pulled randomly for the user. I also had a table (collection in Firebase) for user data where I can track their play history and let them change their gamertag.

# Development Environment

I developed this program using Python and Firebase together. The two work well because they are both pretty simple. There were times I was troubleshooting and I was over thinking things a lot because they were both so simple to work with together.

I used Python for the programming and installed the firebase_admin libraries before starting. You'll also need to set up an account with Firebase.

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [W3Schools](https://www.w3schools.com/)
- [GeeksForGeeks](https://www.geeksforgeeks.org/)
- [Firebase.google.com](https://firebase.google.com/)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

- I want to add more functionality to give users a higher rank after completing a certain number of puzzles.
- Developing more in the database realm would allow for better gameplay. I could add more art or animations for the puzzles.
- I also wanted to develop this on an Android app but I haven't been getting along well enough with Android Studio yet.