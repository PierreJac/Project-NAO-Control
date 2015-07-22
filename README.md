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
- Go to your choregraphe suite folder, then in the bin folder and launch *naoqi-bin* to create a virtual NAO on your computer
     - You can launch several virtual NAO on different ports using :
```sh
$ ./naoqi-bin -p [Port Number] &
```
- Add pynaoqi to your python path or if your using Spyder goto to *->Tools->PYTHONPATH manager* and add a path to the folder containing pynaoqi
- *Optional* : You can launch choregraphe to visualize your virtual NAO or check its IP and Port using the connect button ![Alt Text][id1]
- Launch the v-rep simulation ![AltText][id2]. (or the scripts won't work)
- Launch the multi_nao_control.py script if you have several NAO or the single_nao_control.py if you have just one NAO to control
- Give all the informations needed (IPs and Ports) and wait until *NAO is listening*
- You can try to make your NAO move in v-rep using choregraphe or a script you've made
- Enjoy !

### How to retrieve the video from NAO's vision sensors in v-rep :
You can retrieve images from the cameras of your virtual NAO in v-rep just by using our script vision_sensor.py. This script will stream the camera in a independent display. You can also import the function in another script.
The function getVisionSensor will just retrieve the image and not display it. 

### How to configre your own v-rep scene :
If you want to create your very own v-rep scene containing a NAO, you'll need to configure it so the remote API could connect to it. To do so please follow the official v-rep documentation :
- [Enable remote API client side]
- [Enable remote API server side]
- Or if you prefer you can follow this -> [video] <- (many thanks to Nikolai K. for his really good tutorial)   
In order to get the camera and the fingers working you'll also need a few more steps :
- For the cameras 
  - In the properties of the cameras untick "Explicit Handling"
- For the fingers
  - In each joint properties tick "Motion Handling of all joints enabled" 
  - In each model properties of each joints groupement check that everything is untick  

Finally, disable the child scripts automatically generated with the NAO.


[v-rep]:http://www.coppeliarobotics.com/downloads.html
[Python NAOqi-SDK]:https://community.aldebaran.com/en/resources/software
[Choregraphe Suite]:https://community.aldebaran.com/en/resources/software
[developper program]:https://community.aldebaran.com/en/developerprogram#section3
[Spyder]:https://pypi.python.org/pypi/spyder
[id1]:http://doc.aldebaran.com/2-1/_images/connect-to_button.png
[id2]:http://www.coppeliarobotics.com/helpFiles/en/images/simulation1.jpg
[Enable remote API client side]:http://www.coppeliarobotics.com/helpFiles/en/remoteApiClientSide.htm
[Enable remote API server side]:http://www.coppeliarobotics.com/helpFiles/en/remoteApiServerSide.htm
[video]:https://www.youtube.com/watch?v=SQont-mTnfM&list=PLhEaSBRJaAcyCDyLWYvtOte0RuoovBU2t&index=3