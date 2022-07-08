**Authentication using the device's mac address as login**

libraries : uuid,socket and json

* to install the libs :

1. pip install uuid
2. pip install sockets
3. pip install jsonlib

the idea is to use the Mac address of your custumer device as a login , in case you want to share "or sell XD" a document just for this person and avoid the accounts sharing 

the class "autentif" is composed from 4 functions  "just for the moment* :)"

* CreateAcc() :  let your constumer to create an account the take the mac addres as login and let the user to set a password and confirmed it
* loginAcc(): this function let the user just set the password and check is the user have an account or not with the checkAcc() function
* checkAcc(): function check the validity of both login and password, it return some "invalidity" messages to the user if the login or the passwor is incorrect
* loginExist(): function that check if a device exist in the database it help me to know what I will give the user first (creatacc or login)
