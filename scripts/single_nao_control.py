# -*- coding: utf-8 -*-
"""
@author: Pierre Jacquot
"""
#For more informations please check : http://www.coppeliarobotics.com/helpFiles/en/apiFunctions.htm
import vrep,sys
from naoqi import ALProxy
from manage_joints import get_first_handles,JointControl

print '================ Program Sarted ================'

vrep.simxFinish(-1)
clientID=vrep.simxStart('127.0.0.2',19999,True,True,5000,5)
if clientID!=-1:
	print 'Connected to remote API server'

else:
	print 'Connection non successful'
	sys.exit('Could not connect')


print "================ Choregraphe's Initialization ================"
print 'Enter your NAO IP'
naoIP = raw_input()
#naoIP = map(str,naoIP.split())
print 'Enter your NAO port'
naoPort = raw_input()
naoPort=int(naoPort)
#naoPort = map(int,naoPort.split())

motionProxy = ALProxy("ALMotion",naoIP, naoPort)
postureProxy = ALProxy("ALRobotPosture", naoIP, naoPort)

#Go to the posture StandInitZero
posture = 'StandZero'
print 'Posture Initialization : ' + posture
motionProxy.stiffnessInterpolation('Body', 1.0, 1.0)
postureProxy.goToPosture(posture,1.0,1.0)

Head_Yaw=[];Head_Pitch=[];
L_Hip_Yaw_Pitch=[];L_Hip_Roll=[];L_Hip_Pitch=[];L_Knee_Pitch=[];L_Ankle_Pitch=[];L_Ankle_Roll=[];
R_Hip_Yaw_Pitch=[];R_Hip_Roll=[];R_Hip_Pitch=[];R_Knee_Pitch=[];R_Ankle_Pitch=[];R_Ankle_Roll=[];
L_Shoulder_Pitch=[];L_Shoulder_Roll=[];L_Elbow_Yaw=[];L_Elbow_Roll=[];L_Wrist_Yaw=[]
R_Shoulder_Pitch=[];R_Shoulder_Roll=[];R_Elbow_Yaw=[];R_Elbow_Roll=[];R_Wrist_Yaw=[]
R_H=[];L_H=[];R_Hand=[];L_Hand=[];
Body = [Head_Yaw,Head_Pitch,L_Hip_Yaw_Pitch,L_Hip_Roll,L_Hip_Pitch,L_Knee_Pitch,L_Ankle_Pitch,L_Ankle_Roll,R_Hip_Yaw_Pitch,R_Hip_Roll,R_Hip_Pitch,R_Knee_Pitch,R_Ankle_Pitch,R_Ankle_Roll,L_Shoulder_Pitch,L_Shoulder_Roll,L_Elbow_Yaw,L_Elbow_Roll,L_Wrist_Yaw,R_Shoulder_Pitch,R_Shoulder_Roll,R_Elbow_Yaw,R_Elbow_Roll,R_Wrist_Yaw,L_H,L_Hand,R_H,R_Hand]

get_first_handles(clientID,Body)
print "================ Handles Initialization ================"
commandAngles = motionProxy.getAngles('Body', False)
print '========== NAO is listening =========='

JointControl(clientID,motionProxy,0,Body)
    

