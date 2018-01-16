

# T3室外定位包使用教程（对应ros版本 - kinetic）

--------------


## 安装
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
**ps:如果编译过程中出现缺少某些库，安装对应的库即可。**
## 使用
- 启动机器人端驱动程序。
```cpp
ssh t3@ROBOT_IP
roslaunch turtlebot3_bringup turtlebot3_robot_t3.launch
```
- 在pc端打开对应的导航launch。
```cpp
roslaunch robot_localization ekf_template_navigation_gps.launch
```
## 备注
- 如要使用不同的地图，把地图放到**robot_localization**下的**map**文件夹下，修改文件名为**map.pgm**即可。
- 如要修改地图的原点坐标，修改**robot_localization**下的**map**文件夹下**map.yaml**中的**origin**属性即可。
- 在有gps信号的情况下，机器人的起始坐标点和**map.yaml**中的**origin**必须对应，即当机器人位于origin的坐标点时的gps信号就是机器人真实的起始gps坐标信号。gps起始坐标点在**robot_localization**下的**params**文件夹下**ekf_template_test.yaml**中最下方**datum： [31.262436, 121.615930, 0]** 



robot_localization


robot_localization is a package of nonlinear state estimation nodes. The package was developed by Charles River Analytics, Inc.

Please see documentation here: http://wiki.ros.org/robot_localization
