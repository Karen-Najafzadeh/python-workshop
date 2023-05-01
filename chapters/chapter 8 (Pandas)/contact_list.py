# this will be a cintact list using the help of Pandas

import pandas as pd

# these contacts will have a name, a number and a country
#this program will work like...
# phase one 
# when program is started it will show you the currunt contact list 
# which deals with file handling so we will edit the code and add this fiture later 
#bulshit 
#dont buther :)
# phase two
#the user will be able to choose either to add or delete or even edit their contacts

# so we creat our data frame here
#data = {"name" : ["ali", "mohammad","bahram"],
#        "number" : ["11111111111","45454545454","8585858585"],
#        "country" : ["Iran","India","Iraq"]}
data = {"name" : [],
        "number" : [],
        "country" : []}


#taking first contact

print("let's add your first contact")
def Add():
    data["name"].append(input("\n what is the name? \n"))
    data["number"].append(input("give me their number ... \n"))
    data["country"].append(input("in which country do they live ?\n"))
    dataframe = pd.DataFrame(data)
    print(dataframe)
Add()


print("We just created a new cantact list\n")

while (True):
    user_choise = input ("Now what do you wanna do wi it? \n Add a new contact? (type the word \"Add\") \n Delete a contact? (type the word \"Del\") \n eddit the contact list? (type the word \"Edd\")")
    if (user_choise == "Add"):
        Add()
# defining these functions we used in user_choise

def Del(index):
    dataframe = dataframe.drop(index)

#def Edd():
#    bla bla bla

# do the stuff with the data frame not the dictionary
# of course we can deal with the dictionary and the cast it to a data frame
# but i prefer to deal with the Data Frame directly

pd.concat()