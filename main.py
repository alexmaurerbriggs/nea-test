username = input("What is your username? ")
password = input("What is your password? ")

if (username != 'alexmaurer-briggs' or password != 'oskarisalad'):
    print("Your username or password is incorrect")
    

print("Hello,", username, "you have signed in with your username and password.")

favouriteGenre = input("What is your favourite music genre, from brit pop, rock and pop rock? ")

if (favouriteGenre == 'rock'):
    print("I recommend the songs: Bohemian Rhapsody by Queen and Smells Like Teen Spirit by Nirvana. ")
elif (favouriteGenre == 'brit pop'):
    print("I recommend the songs: Parklife by Blur and Common People by Pulp. ")
elif(favouriteGenre == 'pop rock'):
     print("I recommend the song: Holiday by Green Day. ")

print("All the songs that you could have picked are: ")
break
print("Bohemian Rhapsody by Queen,")
print("Smells Like Teen Spirit by Nirvana,")
print("Parklife by Blur,")
print("Common People by Pulp,")
print("Holiday by Green Day,")
break

first_song = input("Pick one of these songs from all the genres to make a playlist no more than 10 mins long. ")
second_song = input("Another song. ")
third_song = input("One more. ")

print("You have picked", first_song, ",", second_song, "and", third_song, "for your playlist.")

     
