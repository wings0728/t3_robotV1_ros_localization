

#T3室外定位包使用教程（对应ros版本 - kinetic）

--------------


##安装
- 在catkin工作目录下的src文件夹内。
```cpp
cd ~/catkin_ws/src
git clone https://github.com/wings0728/t3_robotV1_ros_localization

```
- `git clone`turtlebot3的程序。
```cpp
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
```
- 编译
```cpp
cd ~/catkin_ws
catkin_make
```
ps:如果编译过程中出现缺少某些库，安装对应的库即可。
##使用

##备注




robot_localization


robot_localization is a package of nonlinear state estimation nodes. The package was developed by Charles River Analytics, Inc.

Please see documentation here: http://wiki.ros.org/robot_localization
