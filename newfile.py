#write a python ptogram to display a user entered name followed by Good Afternoon using input () function.
name=input("enter your name:")
print(f"Good Afternoon,{name}")

#write  aprogram to gill in letter template given below with name and date.
letter=   '''Dear <|Name|>,
               You are selected!
               <|Date|>'''
print(letter.replace("<|Name|>","Duaa").replace("<|Date|>","12 November 2026"))

#Write  a program to detect double space in a string.
name="Duaa is a good   girl"
print (name.find("  "))
              #...if tgere is no double space its shows -1
#Replace the double space from the problem 3 with single spaces.
name="Duaa is a good   girl"
print(name.replace("   "," "))
#Write a program to format the following letter using escape sequence characters.
letter="Dear,\n Duaa.\tYou are doing great\nLove youuu!"
print(letter)
