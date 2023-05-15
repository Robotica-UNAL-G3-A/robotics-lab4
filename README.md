# Robotic's lab 4: Direct kinematics
This repo contains the implementation of the solution to the movement control of Phantom X Pincher. This robot has Dynamixel AX-12 
motor as an actuators. To use them the dynamixel wizard is recommended and the ros-noetic-dynamixel-workbench is requiered to use them with ROS. This repo is build in the form of a ROS package.


## About the robotics-lab4 ROS package
This is package inspired by (blantenly stolen from) the `one-motor-repo`[^one-motor-repo] and the `px repo`[^px repo]. Getting these package would be helpful. After getting them and locating them at catkin/src.


Test if they are correctly working.
```bash
roslaunch -v px_robot px_rviz.launch 
```

```bash
roslaunch dynamixel_one_motor one_controller.launch 

```

To run  this package use the following command

```bash
roslaunch robotics-lab4 dynamixel_control.launch 
```



<!--
waist, shoulder, elbow, wrist
ls /dev/ttyU*

-->


## Setup
### Software configuration 
```
sudo apt install ros-noetic-dynamixel-workbench
```

### Connections
At the lab you are provided with a kit with:
- The  pincher x robot 
- A FTDI interface
- A USB cable extender
- Power supply

1 Connect the FTDI to your computer, ensure that is set up to TTL mode.
2 Check it is being detected `ls /dev/ttyU*` and set the necessary permissions (only the first tiem). 
3 Power up the robot by connecting the power supply to the power jack of the multi connector adapter
4 Connect the FTDI to the multi connector adapter *through any of the available port*
5 Use Dynamixel wizard to check the motors are working correctly


### Troubleshooting
- If after following the steps in the guide[^lab-guide] you have trouble and the motors are not recognize on the Dynamixel wizard. check the cable connection.

- Check Again if the USB is being detected and what permission does it has by running `ls -la /dev/ttyU*
- If problems remain, try disconnecting one of the motor separating it from the reset (out of the daisy chain) and connect it directly to the multi connector adapter. Check if now it is recognized. If the motors have the same ID number they enter into conflict and won't be recognized by the wizard if there is more than one motor with the same ID connected at the same time[^troubleshooting-video]. to solve this, change the ID to a unique value of each of the motors one at the time using the packets tools. This tool allows to communicate with the motor and send commands such as write to registers. Write to register 3 the idea you selected(data length of 1). Other alternative is by following the post referenced below [id-setting].


## Using Docker

USB 

install [usbipd](https://github.com/dorssel/usbipd-win) in the host machine. And follow the instructions

inside the wsl instance 
```
sudo apt install linux-tools-virtual hwdata
sudo update-alternatives --install /usr/local/bin/usbip usbip `ls /usr/lib/linux-tools/*/usbip | tail -n1` 20
```


```
usbipd wsl --help
usbipd wsl list
usbipd wsl attach --busid=<BUSID>
```
## Direct Kinematics
![capture robotStudio signal creation](/media/DK.png)
## Positions
![capture robotStudio signal creation](/media/P1.png)
![capture robotStudio signal creation](/media/P2.png)
![capture robotStudio signal creation](/media/P3.png)
![capture robotStudio signal creation](/media/P4.png)
![capture robotStudio signal creation](/media/P5.png)
## Conclusions 


## Contributors
- [Juan Sebastian Duenas](https://github.com/jsduenass) (jsduenass@unal.edu.co)
- [German Andres Urbina Gutierrez](https://github.com/gurbinaUn)  (gurbina@unal.edu.co)
- [Brayan Daniel Barrera Galvis](https://github.com/brayandan) (bdbarrerag@unal.edu.co)

## Reference
[^lab-guide]:[Lab guide ](https://github.com/fegonzalez7/rob_unal_clase3)
[^one-motor-repo]: [dynamixel one motor](https://github.com/fegonzalez7/dynamixel_one_motor)
[^px repo]: [px repo](https://github.com/felipeg17/px_robot)
[^troubleshooting-video]:[dynamixel troubleshooting video ](https://www.youtube.com/watch?v=LN2XjlSr1kM&t=94s)
[^id-setting]:[setting id dynamixel](https://forum.robotis.com/t/setting-id-s-on-your-new-dynamixel/723)
- [rqt gui tutorial](https://github.com/ChoKasem/rqt_tut)
[^callback]:[rqt buttons callbacks](https://answers.ros.org/question/195152/how-to-add-callbacks-for-a-qtwidget-in-ros/)

