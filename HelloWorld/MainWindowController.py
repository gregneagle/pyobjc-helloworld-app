# -*- coding: utf-8 -*-
#
#  MainWindowController.py
#  HelloWorld
#
#  Created by Greg Neagle on 3/19/19.
#  Copyright (c) 2019 Greg Neagle. All rights reserved.
#

from Foundation import *
from AppKit import *

from objc import YES, NO, IBAction, IBOutlet, nil

class MainWindowController(NSWindowController):

    labelField = IBOutlet()
    quitButton = IBOutlet()
    
    def awakeFromNib(self):
        self.labelField.setStringValue_("Hello, World!")

    @IBAction
    def quitButtonClicked_(self, sender):
        NSApp.terminate_(self)

