#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool, CommandBoolRequest, SetMode, SetModeRequest
from math import cos, sin

current_state = State()

def state_cb(msg):
    global current_state
    current_state =msg

if __name__== "__main__":
    rospy.init_node("circle_trajectory_node")

state_sub = rospy.Subscriber("mavros/state", State, callback=state_cb)
local_pos_pub = rospy.Publisher("mavros/setpoint_position/local", PoseStamped, queue_size=10)

# Setpoint publishing MUST be faster than 2Hz
rate = rospy.Rate(20)

# Wait for Flight Controller connection
while not rospy.is_shutdown() and not current_state.connected:
    rate.sleep()

while not rospy.is_shutdown():
    # 원의 중심 좌표와 반지름 설정
    center_x = 0.0
    center_y = 0.0
    radius = 2.0

    # 현재 시간을 사용하여 원을 그리는 경로 계산
    current_time = rospy.Time.now()
    angle = current_time.to_sec()  # 시간을 각도로 변환
    x = center_x + radius * cos(angle)
    y = center_y + radius * sin(angle)

    # 원 위를 움직이는 드론의 목표 위치 설정
    pose = PoseStamped()
    pose.pose.position.x = x
    pose.pose.position.y = y
    pose.pose.position.z = 2.0  # z 축은 원하는 높이로 설정

    local_pos_pub.publish(pose)
    rate.sleep()