#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
threading


"""

import threading
class ThController( threading.Thread ):

   # Override Thread's __init__ method to accept the parameters needed:
    def __init__( self,parent):
        self.parent = parent
        threading.Thread.__init__ ( self )

    def run ( self ):
        while self.parent.ctrlattive:
            j=json.loads(data)
            self.parent.data=j