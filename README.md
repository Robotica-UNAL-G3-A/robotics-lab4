# robotic lab4 Direct kinematics

The idea behind this lab is to control the movement of Phantom X Pincher.

waist, shoulder, elbow, wrist
Dynamixel AX-12 

FTDI troubleshooting


```bash
roslaunch -v px_robot px_rviz.launch 
```

```bash
roslaunch dynamixel_one_motor one_controller.launch 
```


```bash
roslaunch robotics-lab4 dynamixel_control.launch 
```

ls /dev/ttyU*

## Conclusions 


## Contributors
- [Juan Sebastian Duenas](https://github.com/jsduenass) (jsduenass@unal.edu.co)
- [German Andres Urbina Gutierrez](https://github.com/gurbinaUn)  (gurbina@unal.edu.co)
- [Brayan Daniel Barrera Galvis](https://github.com/brayandan) (bdbarrerag@unal.edu.co)

## Reference
- [Lab guide ](https://github.com/fegonzalez7/rob_unal_clase3)
- [dynamixel one motor](https://github.com/fegonzalez7/dynamixel_one_motor)
- [px repo](https://github.com/felipeg17/px_robot)
- [dynamixel troubleshooting video ](https://www.youtube.com/watch?v=LN2XjlSr1kM&t=94s)
- [setting id dynamixel](https://forum.robotis.com/t/setting-id-s-on-your-new-dynamixel/723)