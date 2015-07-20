# Project NAO Control
This project goal is to simulate a NAO in v-rep.
The main idea is to be able to test a script in a virtual environment before implementing it on a real NAO.
In addition to v-rep we will use the Choregraphe suite and the Python NAOqi SDK from Aldebaran.

### Requirements
- [v-rep] : A mostly free and awsome robot simulator.
- [Python NAOqi-SDK] : Contain all the function you need to manipulate your NAO (virtual or not) using python.
- [Choregraphe Suite] : This will allow you to manipulate your virtual robot easier and launch a virtual NAO on your computer.
- [Spyder] : This is not mandatory, but it's a good MATLAB-like development environment for python

> N.B : To download the Aldebaran related softwares you must pocess a NAO or join their [developper program]

### Quickstart guide
- Launch v-rep and load the scene contained in the *Vrep-scene* folder
- Launch *naoqi-bin* contained in the bin folder of your choregraphe suite folder to create a virtual NAO on your computer
     - You can launch several virtual NAO on different ports using :
```sh
$ ./naoqi-bin -p [Port Number] &
```
- Add naoqi to your python path or in Spyder goto to *->Tools->PYTHONPATH manager* and add a path to the folder containing pynaoqi
- Optional : You can launch choregraphe to visualize your virtual NAO or check is IP and Port using the connect button ![Alt Text][id1]
- Launch the v-rep simulation ![AltText][id2]
- Launch the multi_nao_control.py script if you have several NAO or the single_nao_control.py if you have just one NAO to control
- Give all the informations needed (IPs and Ports) and wait until *NAO is listening*
- You can try to make your NAO move using choregraphe or a script you've made

[v-rep]:http://www.coppeliarobotics.com/downloads.html
[Python NAOqi-SDK]:https://community.aldebaran.com/en/resources/software
[Choregraphe Suite]:https://community.aldebaran.com/en/resources/software
[developper program]:https://community.aldebaran.com/en/developerprogram#section3
[Spyder]:https://pypi.python.org/pypi/spyder
[id1]:http://doc.aldebaran.com/2-1/_images/connect-to_button.png
[id2]:http://www.coppeliarobotics.com/helpFiles/en/images/simulation1.jpg