import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from numpy import pi
import numpy as np

def dinamixel_dummy():
    rospy.init_node('dinamixel_dummy', anonymous=False)
    
    jTrajecSub = rospy.Subscriber('/joint_trajectory', JointTrajectory, callback)
    
    jStatePub = rospy.Publisher("/dynamixel_workbench/joint_states", JointState,queue_size=0)

    while not rospy.is_shutdown():
        pass
    #rospy.spin()
    

def callback(traject_msg):
    state_msg = JointState()
    state_msg.header.stamp = rospy.Time.now()

    state_msg.name = "dummy dinamixel"
    state_msg.position = [ 1, 2, 3, 4, 5]
    state_msg.velocity = [ 0, 0, 0, 0, 0]
    state_msg.effort = [ 0, 0, 0]

    jStatePub.publish(state_msg)
    
    print(state_msg)

    


if __name__ == '__main__':
    try:
        dinamixel_dummy()
    except rospy.ROSInterruptException:
        pass