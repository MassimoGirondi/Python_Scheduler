#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class process(object):
    pid=-1
    enter=-1
    remaining=-1
    tt=-1
    tr=-1
    tw=-1
    def __init__(self, pid, enter, remaining):
        self.pid=pid
        self.enter=enter
        self.remaining=remaining
