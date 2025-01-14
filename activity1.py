print("we are lerning about funcyions")
def hello():
    return "hello guys"

print(hello())
name=str(input("whase is your name: "))
name =  name.capitalize()
if name == "Reda":
    print (f"{hello()} {name}")
else:
    who = str(input("who are you ?"))