def greet():
 return "hello" # Return function can be used as a predessor at some point as given below. And using this function will only recall the statement given in it. Not whole "def" function.
 


print(greet(),"Ashish Jain") # The output of this clause will be "hello Ashish Jain"


def greet(lang):
    if lang == "es":
        return "hola"
    elif lang == "fr":  # This function can be also use like this as per this example. 
        return "bonjour"
    else:
        return "hello"

lg = input("enter you language preference default is English and for espanol type 'es' and for french type 'fr'.")
name = input("enter your name")

print(greet(lg),name)