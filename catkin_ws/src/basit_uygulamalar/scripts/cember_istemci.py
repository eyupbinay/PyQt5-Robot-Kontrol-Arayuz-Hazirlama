#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 20:07:53 2022

@author: eyup
"""

"""
Uygulama 3: Çember Boyunca Hareket - Server Düğümü
"""

import rospy
from basit_uygulamalar.srv import CemberHareket

rospy.wait_for_service("cember_servis")
try:
    yaricap=float(input("Yaricap giriniz: "))
    servis=rospy.ServiceProxy("cember_servis",CemberHareket)
    servis(yaricap)

except rospy.ServiceException:
    print("servisle alakali hata meydana geldi !!!")