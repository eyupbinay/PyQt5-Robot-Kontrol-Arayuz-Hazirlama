#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 18:37:43 2022

@author: eyup
"""

"""
Uygulama 6: Lazer Sensörden Gelen Veriyi Kullanma
"""

import rospy
from sensor_msgs.msg import LaserScan


class LazerVerisi():
    def __init__(self):
        rospy.init_node("lazer_dugumu")
        rospy.Subscriber("scan", LaserScan ,self.lazerCallback)
        rospy.spin()
        
        
    def lazerCallback(self,mesaj):
        sol_on=list(mesaj.ranges[0:9])
        sag_on=list(mesaj.ranges[350:359])
        on=sol_on + sag_on
        sol=list(mesaj.ranges[80:100])
        sag=list(mesaj.ranges[260:280])
        arka=list(mesaj.ranges[170:190])
        min_on=min(on)
        min_sol=min(sol)
        min_sag=min(sag)
        min_arka=min(arka)
        print(min_on,min_sol,min_sag,min_arka)
        
nesne=LazerVerisi()