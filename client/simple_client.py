# *-* coding: iso-8859-1 *-*

# Définition d'un client réseau rudimentaire
# Ce client dialogue avec un serveur ad hoc

import socket, sys

HOST = '127.0.0.1'
PORT = 50000
BUFFER_SIZE = 1024

# 1) création du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2) envoi d'une requête de connexion au serveur :
try:
    mySocket.connect((HOST, PORT))
except socket.error:
    print "La connexion a échoué."
    sys.exit()    
print "Connexion établie avec le serveur."    

# 3) Dialogue avec le serveur :
msgServeur = mySocket.recv(BUFFER_SIZE)

while 1:
    if msgServeur.upper() == "FIN" or msgServeur =="":
        break
    print "S>", msgServeur
    msgClient = raw_input("C> ")
    mySocket.send(msgClient)
    msgServeur = mySocket.recv(BUFFER_SIZE)

# 4) Fermeture de la connexion :
print "Connexion interrompue."
mySocket.close()
