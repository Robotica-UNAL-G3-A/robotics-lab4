#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from numpy import pi
import numpy as np

class dinamixel_dummy():
    def __init__(self):
        
        self.jTrajecSub = rospy.Subscriber('/joint_trajectory', JointTrajectory, self.trajec_callback)
        
        self.jStatePub = rospy.Publisher("/dynamixel_workbench/joint_states", JointState,queue_size=0)
        rospy.loginfo("dinamixel dummy start")
        #rospy.spin()
    
        while not rospy.is_shutdown():
            
            #rospy.sleep(1)
            pass
    

    def trajec_callback(self,traject_msg):
        print(traject_msg)
        pos = traject_msg.points[0].positions
        state_msg = JointState()
        state_msg.header.stamp = rospy.Time.now()

        state_msg.name = "dummy dinamixel"
        state_msg.position = pos
        state_msg.velocity = [ 0, 0, 0, 0, 0]
        state_msg.effort = [ 0, 0, 0]

        self.jStatePub.publish(state_msg)
        print(state_msg)
        print(state_msg)

    


if __name__ == '__main__':
    
    rospy.init_node('dinamixel_dummy',anonymous=False)
    try:
        
        node_dummy = dinamixel_dummy()
    except rospy.ROSInterruptException:
        pass