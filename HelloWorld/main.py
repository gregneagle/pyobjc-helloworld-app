# -*- coding: utf-8 -*-
#
#  main.py
#  HelloWorld
#
#  Created by Greg Neagle on 3/19/19.
#  Copyright (c) 2019 Greg Neagle. All rights reserved.
#

# import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import AppDelegate
import MainWindowController

# pass control to AppKit
AppHelper.runEventLoop()
