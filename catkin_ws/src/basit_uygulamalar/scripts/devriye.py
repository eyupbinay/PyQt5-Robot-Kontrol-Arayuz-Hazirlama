#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 20:59:21 2022

@author: eyup
"""

"""
Uygulama 4: Devriye Gezme
"""

import rospy
from geometry_msgs.msg import Twist

def volta():
    rospy.init_node("volta_at")
    pub=rospy.Publisher("cmd_vel",Twist,queue_size=10)
    hiz_mesaji=Twist()
    robot_hiz=0.25
    volta_uzunluk=rospy.get_param("/VoltaUzunluk")
    volta_sayisi=rospy.get_param("/VoltaSayisi")
    sayici=0
    rospy.loginfo("devriye gezmeye baslandı !!!")
    
    while sayici < volta_sayisi:
        t0=rospy.Time.now().to_sec()
        yer_degistirme=0
        if sayici %2 ==0:
            hiz_mesaji.linear.x=robot_hiz
        else:
            hiz_mesaji.linear.x=-robot_hiz
            
            
        while yer_degistirme< volta_uzunluk:
            pub.publish(hiz_mesaji)
            t1=rospy.Time.now().to_sec()
            yer_degistirme=robot_hiz*(t1-t0)
        hiz_mesaji.linear.x=0
        pub.publish(hiz_mesaji)
        sayici=sayici + 1
        
    rospy.loginfo("Devriye tamamlandi !")
    rospy.is_shutdown()
    
    
volta()