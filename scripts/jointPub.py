import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from numpy import pi

# 0 -> 150
# 1 -> 200
# -1 -> 91.

def joint_publisher():
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)
    
    while not rospy.is_shutdown():
        state = JointTrajectory()
        
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_5"]
        point = JointTrajectoryPoint()
        select_position = int(input(" Enter desired position:  \n"))
        point.positions = pi/180.0*choose_position(select_position)

        point.time_from_start = rospy.Duration(0.5)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        print(state)

        rospy.sleep(1)
def choose_position(select_position):
    
    PHome = [  0,  0,   0,  0, 0]
    P0 =  [  0,  0,   0,  0, 0]
    P1 =  [-25, 15, -20, 20, 0]
    P2 =  [ 35,-35, 30, -30, 0]
    P3 =  [ -85, 20, -55, 17, 0]
    P5 =  [-80, 35, -55, 45, 0]
    if(select_position==1) :
        return P1
    elif(select_position==2):
        return P2
    elif(select_position==3):
        return P3 
    elif(select_position==4):
        return P4 
    elif(select_position==5):
        return P5
    else:
        return PHome    
        
    


if __name__ == '__main__':
    try:
        joint_publisher()
    except rospy.ROSInterruptException:
        pass