# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 14:00:59 2015

@author: Pierre Jacquot
"""

import sys,vrep,time
from manage_joints import get_new_nao_handles,get_first_handles,JointControl
from naoqi import ALProxy
from threading import Thread

print 'Enter the number of Nao which are connected on your network : '
nbrOfNao= raw_input()
nbrOfNao = int(nbrOfNao)
print 'Enter their IP adresses (separated with one space)'
naoIP = raw_input()
naoIP = map(str,naoIP.split())
print 'Enter their ports (respectively to the order of the IPs and separated with one space)'
naoPort = raw_input()
naoPort = map(int,naoPort.split())

#Connexion to VRep
print '================ Connexion to VRep ================'
vrep.simxFinish(-1)
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) 
if clientID!=-1:
    print 'Connected to remote API server'

else:
    print 'Connection non successful'
    sys.exit('Could not connect')

print '================ Initialization of the first NAO ================'
#Handles first initialization
Head_Yaw=[];Head_Pitch=[];
L_Hip_Yaw_Pitch=[];L_Hip_Roll=[];L_Hip_Pitch=[];L_Knee_Pitch=[];L_Ankle_Pitch=[];L_Ankle_Roll=[];
R_Hip_Yaw_Pitch=[];R_Hip_Roll=[];R_Hip_Pitch=[];R_Knee_Pitch=[];R_Ankle_Pitch=[];R_Ankle_Roll=[];
L_Shoulder_Pitch=[];L_Shoulder_Roll=[];L_Elbow_Yaw=[];L_Elbow_Roll=[];L_Wrist_Yaw=[]
R_Shoulder_Pitch=[];R_Shoulder_Roll=[];R_Elbow_Yaw=[];R_Elbow_Roll=[];R_Wrist_Yaw=[]
R_H=[];L_H=[];R_Hand=[];L_Hand=[];
Body = [Head_Yaw,Head_Pitch,L_Hip_Yaw_Pitch,L_Hip_Roll,L_Hip_Pitch,L_Knee_Pitch,L_Ankle_Pitch,L_Ankle_Roll,R_Hip_Yaw_Pitch,R_Hip_Roll,R_Hip_Pitch,R_Knee_Pitch,R_Ankle_Pitch,R_Ankle_Roll,L_Shoulder_Pitch,L_Shoulder_Roll,L_Elbow_Yaw,L_Elbow_Roll,L_Wrist_Yaw,R_Shoulder_Pitch,R_Shoulder_Roll,R_Elbow_Yaw,R_Elbow_Roll,R_Wrist_Yaw,L_H,L_Hand,R_H,R_Hand]
#Proxy creation
motionProxy=[];postureProxy=[]

get_first_handles(clientID,Body)
#Get the Handle of the whole NAO in VRep
NAO_Handle = vrep.simxGetObjectHandle(clientID,'NAO',vrep.simx_opmode_oneshot_wait)
#Get the absolute position of the first NAO
NAO_pos = vrep.simxGetObjectPosition(clientID,NAO_Handle[1],-1,vrep.simx_opmode_streaming)[1]

print 'You have ' + str(nbrOfNao) + ' NAO connected'


#Proxy initialization
if nbrOfNao == 1:
    motionProxy.append(ALProxy('ALMotion',naoIP[0],naoPort[0]))
    postureProxy.append(ALProxy('ALRobotPosture', naoIP[0], naoPort[0]))
else:
    motionProxy.append(ALProxy('ALMotion',naoIP[0],naoPort[0]))
    postureProxy.append(ALProxy('ALRobotPosture', naoIP[0], naoPort[0]))
    y=0.8
    #Pause the simulation to avoid collision problems
    vrep.simxPauseSimulation(clientID,vrep.simx_opmode_oneshot)
    time.sleep(2)
    for i in range(0,nbrOfNao-1):
        motionProxy.append(ALProxy('ALMotion',naoIP[i+1],naoPort[i+1]))
        postureProxy.append(ALProxy('ALRobotPosture', naoIP[i+1], naoPort[i+1]))
        #Create new NAo in VRep    
        vrep.simxCopyPasteObjects(clientID,NAO_Handle,vrep.simx_opmode_oneshot_wait)
        #Get the handle of the new NAO
        copyNAO = vrep.simxGetObjectHandle(clientID,'NAO#'+str(i),vrep.simx_opmode_oneshot_wait)    
        #Change the position of the new NAO so it won't collide with others    
        vrep.simxSetObjectPosition(clientID,copyNAO[1],-1,[0,y,0.3518],vrep.simx_opmode_oneshot )
        y+=0.8
    #Restart the simulation
    vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot)
    
print '================ Posture Initialization ================'
#Go to the posture StandZero
print 'Posture Initialization : StandZero'
for i in range(0,nbrOfNao):
    motionProxy[i].stiffnessInterpolation('Body', 1.0, 1.0)
    postureProxy[i].goToPosture('StandZero',1.0,1.0)

print '================ Handle Creation for the new NAO ================'
a=vrep.simxGetObjectGroupData(clientID,vrep.sim_object_joint_type,0,vrep.simx_opmode_oneshot_wait)
get_new_nao_handles(nbrOfNao,clientID,Body)
thread=[]
for i in range(0,nbrOfNao):
    thread.append(Thread(target = JointControl, args=(clientID,motionProxy[i],i,Body)))
    thread[i].start()
    print 'Nao number ' + str(i+1) + ' initialized'
print '================ All the Nao are listening ================'