# my python story


def greeting():
    print("HEllo....")
    response=input('do you want to play? (yes/no)')
    return response

def second_choice():
    print("Great....")
    responce=input ('do you open it?...')
    return responce
def haters():               #exist the game
    print("lame,bye then")

def opened():
    print("Great........")
                            #Enter your code here 
def not_opened():
    print("you did it")
   

x = greeting()              #Begin the story


print(x)
if x=="yes": 
    y = second_choice()
    if y=="yes":
        opened()
    elif y=="mabye":
        print("OK........")
    else:
            not_opened()
else:
    haters()

