#the libraries I use in this master piece XD
from getpass import getpass
import uuid
import socket 
import json

#setting my class :)
class ipautantif :
    def __init__(self) :
        self.login = hex(uuid.getnode())
        self.hostname = socket.gethostname()
        #the path to your json file here
        self.path="database.json"

    #function that create an account by taking the mac address as login
    def CreateAcc(self):
        with open(self.path) as f:
            obj = json.load(f)
        print("Welcome "+self.hostname+" ,you can create easily a secret account now")
        print("we already took you MAC address as login, just set a password")
        password = getpass("set your password : ")
        confirmedPass = getpass("comfirm your password : ")
        while(password != confirmedPass) : 
            print("the password and the confirmed pass are not same !!")
            password = getpass("set a password : ")
            confirmedPass = getpass("comfirm your password : ")
        
        obj["accounts"].append({"login":[self.login,password]})
        with open(self.path,"w+") as of:
            json.dump(obj,of)
        print("your account was create succesfully !!")
        
    def checkAcc(self,data,val,password):
        var = 0
        for data in data['accounts'] :
            if(data["login"][0]==val):
                acc = data["login"]
                if(acc[1]== password):
                        var = 1   
                else:
                        var = 2 
                        print( "password incorrect")
            else:
                print("login infounded")
        return var
    #the login function 
    def loginAcc(self):
        print("hello "+self.hostname)
        with open(self.path, 'r') as file:
            data = json.load(file)
        password = getpass("password : ")
        checked = self.checkAcc(data,self.login,password)
        if checked == 2:
            while (checked == 2):
                password = getpass("reinsert pass : ")
                checked = self.checkAcc(data,self.login,password)
        if(checked == 1 ):
            print("start process")
        else : 
            print("you dont have access to this comm")
    def loginExist(self):
        with open(acc.path, 'r') as file:
            data = json.load(file)
        for data in data['accounts'] :
            if(data["login"][0]==self.login):
                return True
        return False


#inplemantation of my code :)
acc = ipautantif()
if (not acc.loginExist()):
    acc.CreateAcc()

acc.loginAcc()


