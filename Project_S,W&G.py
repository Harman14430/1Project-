computer=-1
youstr =input("Enter your choice:")
youDict={"s":1,"w":-1,"g":0}
you=youDict[youstr]
if(computer== you):
     print("draw")

if(computer ==-1 and you==1 ):
    print("you wins")
elif(computer ==-1 and you ==0):
    print("you loose")
if(computer ==1 and you==-1 ):
    print("you loose")
elif(computer ==1 and you==0 ):
    print("you wins")
if(computer ==0 and you==1 ):
    print("you loose")
elif(computer ==0 and you==-1 ):
    print("you wins")
else:
    print("something went wrong")