# SITL_simple_offb_test

터미널1 (가재보 시뮬레이션 시작 및 오프보드모드 변경)
roslaunch px4 mavros_posix_sitl.launch
commander takeoff
commander mode offboard


터미널2 (제어 코드 실행)
rosrun [pakage] [code]

터미널3 (실시간 loacl pose 확인)
rostopic echo /mavros/local_position/pose

**터미널4 (제어코드실행x,position 변경 후 오프보드 모드 변경)
rostopic pub -r 10 /mavros /setpoint_position/local (더블탭 누르기)
