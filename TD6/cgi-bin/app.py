#!/usr/bin/python3
import cgi,cgitb,sys,os


form = cgi.FieldStorage()
print("Content-type: text/html;charset=utf-8\n")
print()

name = form.getvalue('name')
first_name  = form.getvalue('firstname')
e_mail = form.getvalue('email')
society  = form.getvalue('society')
phone_number = form.getvalue('phone_number')
arrival = form.getvalue('arrival')
departure  = form.getvalue('departure')
if(arrival != None):
    arrival = arrival.replace("T"," ")
else :
    arrival = "Non indiqué"
if(departure != None):
    departure = departure.replace("T"," ")
else:
    departure = "Non indiqué"



print("<h1>Inscription entregistré</h1>")
print("<h2>6 ème congrès de la FFFF</h2>")
print("%s %s<br>" % (name,first_name))
print("%s<br><br>" % e_mail)
print("%s<br>" % society)
print("%s<br>" % phone_number)
print("Arrivée : %s<br>" % arrival)
print("Départ : %s<br>" % departure)
print("")

path_file = "cgi-bin/register.svg"
f=open(path_file,"a")
if(os.stat(path_file).st_size==0):
    f.write("Nom | Prénom | Email | Société | Téléphone | Arrivée | Départ")
f.write("\n%s |%s |%s |%s |%s |%s |%s |" % (name,first_name,e_mail,society,phone_number,arrival,departure))
f.close()