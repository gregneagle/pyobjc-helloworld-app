# -*- coding: utf-8 -*-
#
#  AppDelegate.py
#  HelloWorld
#
#  Created by Greg Neagle on 3/19/19.
#  Copyright (c) 2019 Greg Neagle. All rights reserved.
#

from Foundation import *
from AppKit import *

class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
