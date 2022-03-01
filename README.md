# PW_CRACKER_PROTOTYPE2
/
import random
import time
 
Zeichen = [1,2,3,4,5,6,7,8,9,0,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","!",'"',"§","$","%","&","/","(",")","=","?","´","`","{","[","]","}","<",">","|",",",";",":",".","-","_","+","*","~","#","'","^","°"]
Fehlversuche = [0]
 
passwort = str(input("Gib dein Passwort ein: "))   

length_pw = len(passwort)
l_pw = int(length_pw)

f = open("Passwords.txt", "w")

flag = 0
tries = 0
if l_pw == 1:
    for i in range(100000):
        random.choice(Zeichen)
        time.sleep(0.00002)
        for i in range(5):
            time.sleep(0.00002)
            tries += 1
            rn1 = str(random.choice(Zeichen))
            rn = rn1
            if str(rn) == passwort:
                print("Dein Passwort war: "+passwort)
                print("Versuche: "+str(tries))
                f.close()
                quit()
            elif str(rn) != passwort:
                if(str(rn) in Fehlversuche):
                    pass
                else:
                    print(rn)
                    Fehlversuche.append(str(rn))
                    f.write("[ "+str(rn)+" ] ")
elif l_pw == 2:
    for i in range(100000):
        random.choice(Zeichen)
        time.sleep(0.00002)
        for i in range(5):
            time.sleep(0.00002)
            tries += 1
            rn1 = str(random.choice(Zeichen))
            rn2 = str(random.choice(Zeichen))
            rn = rn1+rn2
            if str(rn) == passwort:
                print("Dein Passwort war: "+passwort)
                print("Versuche: "+str(tries))
                f.close()
                quit()
            elif str(rn) != passwort:
                if(str(rn) in Fehlversuche):
                    pass
                else:
                    print(rn)
                    Fehlversuche.append(str(rn))
                    f.write("[ "+str(rn)+" ] ")
elif l_pw == 3:
    for i in range(100000):
        random.choice(Zeichen)
        time.sleep(0.00002)
        for i in range(5):
            time.sleep(0.00002)
            tries += 1
            rn1 = str(random.choice(Zeichen))
            rn2 = str(random.choice(Zeichen))
            rn3 = str(random.choice(Zeichen))
            rn = rn1+rn2+rn3
            if str(rn) == passwort:
                print("Dein Passwort war: "+passwort)
                print("Versuche: "+str(tries))
                f.close()
                quit()
            elif str(rn) != passwort:
                if(str(rn) in Fehlversuche):
                    pass
                else:
                    print(rn)
                    Fehlversuche.append(str(rn))
                    f.write("[ "+str(rn)+" ] ")
elif l_pw == 4:
    for i in range(100000):
        random.choice(Zeichen)
        time.sleep(0.00002)
        for i in range(5):
            time.sleep(0.00002)
            tries += 1
            rn1 = str(random.choice(Zeichen))
            rn2 = str(random.choice(Zeichen))
            rn3 = str(random.choice(Zeichen))
            rn4 = str(random.choice(Zeichen))
            rn = rn1+rn2+rn3+rn4
            if str(rn) == passwort:
                print("Dein Passwort war: "+passwort)
                print("Versuche: "+str(tries))
                f.close()
                quit()
            elif str(rn) != passwort:
                if(str(rn) in Fehlversuche):
                    pass
                else:
                    print(rn)
                    Fehlversuche.append(str(rn))
                    f.write("[ "+str(rn)+" ] ")
elif l_pw == 5:
    for i in range(100000):
        random.choice(Zeichen)
        time.sleep(0.00002)
        for i in range(5):
            time.sleep(0.00002)
            tries += 1
            rn1 = str(random.choice(Zeichen))
            rn2 = str(random.choice(Zeichen))
            rn3 = str(random.choice(Zeichen))
            rn4 = str(random.choice(Zeichen))
            rn5 = str(random.choice(Zeichen))
            rn = rn1+rn2+rn3+rn4+rn5
            if str(rn) == passwort:
                print("Dein Passwort war: "+passwort)
                print("Versuche: "+str(tries))
                f.close()
                quit()
            elif str(rn) != passwort:
                if(str(rn) in Fehlversuche):
                    pass
                else:
                    print(rn)
                    Fehlversuche.append(str(rn))
                    f.write("[ "+str(rn)+" ] ")
elif l_pw == 6:
    for i in range(100000):
        random.choice(Zeichen)
        time.sleep(0.00002)
        for i in range(5):
            time.sleep(0.00002)
            tries += 1
            rn1 = str(random.choice(Zeichen))
            rn2 = str(random.choice(Zeichen))
            rn3 = str(random.choice(Zeichen))
            rn4 = str(random.choice(Zeichen))
            rn5 = str(random.choice(Zeichen))
            rn6 = str(random.choice(Zeichen))
            rn = rn1+rn2+rn3+rn4+rn5+rn6
            if str(rn) == passwort:
                print("Dein Passwort war: "+passwort)
                print("Versuche: "+str(tries))
                f.close()
                quit()
            elif str(rn) != passwort:
                if(str(rn) in Fehlversuche):
                    pass
                else:
                    print(rn)
                    Fehlversuche.append(str(rn))
                    f.write("[ "+str(rn)+" ] ")
