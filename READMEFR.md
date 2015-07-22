# Projet NAO Control
Le but de ce projet est de simuler un NAO sous v-rep.
L'idée est d'être capable de tester un script dans un environnement virtuel avant de l'implémenter dans un NAO réel.
En plus de v-rep, nous allons utiliser la suite de logiciels Choregraphe et le SDK NAOqi en Python.

### Prérequis
- [v-rep] : Un super simulateur de robotique majoritairement gratuit
- [Python NAOqi-SDK] : Contient toutes les fonctions dont vous avez besoin pour manipuler votre NAO (virtuel ou non) utilisant python.
- [Suite de logiciels Choregraphe] : Cela vous permettra de manipuler votre robot virtuel plus aisément et de lancer un NAO virtuel sur votre ordinateur.
- [Spyder] : Ce n'est pas obligatoire, mais c'est un bon environnement de développement proche de MATLAB mais pour le langage python. 

> N.B : Pour télécharger les logiciels liés à Aldebaran , vous devez posséder un NAO ou rejoindre leur [programme de développement]

### Guide pour démarrer rapidement
- Lancez v-rep et chargez la scène contenue dans le dossier *Vrep-scene*
- Allez dans votre répertoire contenant la suite de logiciels Choregraphe, puis dans le dossier bin et lancez *naoqi-bin* afin de créer un NAO virtuel sur votre ordinateur
     - Vous pouvez lancer plusieurs NAO virtuels sur différents Ports en utilisant :
```sh
$ ./naoqi-bin -p [Numéro de Port] &
```
- Ajoutez pynaoqi dans votre chemin python (PYTHONPATH) ou si vous utilisez Spyder allez dans *->Outils->Gestionnaire de PYTHONPATH* et ajoutez le chemin du dossier contenant pynaoqi
- *Optionnel* : Vous pouvez lancer Choregraphe pour visualiser votre NAO virtuel ou vérifier son adresse IP et son Port en utilisant le bouton de connexion ![Alt Text][id1]
- Lancez la simulation v-rep ![AltText][id2] (sinon les scripts ne fonctionneront pas)
- Lancez le script multi_nao_control.py si vous avez plusieurs NAO ou single_nao_control.py si vous  avez seulement un NAO à contrôler
- Donnez toutes les informations nécessaires (adresses IP et Ports) et attendez jusqu'à voir apparaître *NAO is listening*
- Vous pouvez essayer de faire bouger votre NAO dans v-rep en utilisant Choregraphe ou un script que vous avez fait. 
- Enjoy !

### Comment recevoir les images des caméras du NAO virtuel de v-rep 
Vous pouvez récupérer les images des caméras du NAO virtuel dans v-rep juste en utilisant notre script vision_sensor.py. Ce script diffusera en streaming la caméra dans une nouvelle fenêtre. Vous pouvez aussi importer la fonction dans un autre script. La fonction getVisionSensor récupérera simplement l'image mais ne l'affichera pas.
### Comment configurer votre propre scène v-rep:
Si vous voulez créer votre scène v-rep personnelle contenant un NAO, vous devrez la configurer afin que l'API distante puisse s'y connecter. Pour le faire, suivez la documentation officielle de v-rep:  
- [Activer l'API distante du côté client]
- [Activer l'API distante du côté serveur]
- Ou si vous préférez, vous pouvez suivre cette -> [vidéo] <-    
Afin d'avoir les caméras et les doigts du NAO fonctionnels, vous allez également avoir besoin de suivre d'autres étapes:
- Pour les caméras 
  - Dans les propriétés des caméras décochez "Explicit Handling" 
- Pour les doigts
  - Dans les propriétés de chaque articulation cochez "Motion Handling of all joints enabled" 
  - Dans chaque "model properties" de chaque groupement d'articulations vérifiez que tout est décoché  
  
Finalement, désactivez le script généré automatiquement avec le NAO.

[v-rep]:http://www.coppeliarobotics.com/downloads.html
[Python NAOqi-SDK]:https://community.aldebaran.com/en/resources/software
[Suite de logiciels Choregraphe]:https://community.aldebaran.com/en/resources/software
[programme de développement]:https://community.aldebaran.com/en/developerprogram#section3
[Spyder]:https://pypi.python.org/pypi/spyder
[id1]:http://doc.aldebaran.com/2-1/_images/connect-to_button.png
[id2]:http://www.coppeliarobotics.com/helpFiles/en/images/simulation1.jpg
[Activer l'API distante du côté client]:http://www.coppeliarobotics.com/helpFiles/en/remoteApiClientSide.htm
[Activer l'API distante du côté serveur]:http://www.coppeliarobotics.com/helpFiles/en/remoteApiServerSide.htm
[vidéo]:https://www.youtube.com/watch?v=SQont-mTnfM&list=PLhEaSBRJaAcyCDyLWYvtOte0RuoovBU2t&index=3



