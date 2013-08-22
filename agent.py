from msgmanager import *
import logging

class Agent:
    def __init__(self, team_name):
        self.team_name = team_name
        self.msg_manager = MsgManager()

        # the plan
        self.cmds = []
        # info objects
        self.body_info = None
        self.aural_info = None
        self.vision_info = None

    def connect(self):
        msg = '(init {0})'.format(self.team_name)
        self.msg_manager.send(msg)

    def run(self):
        while True:
            print 'before read'
            info = self.msg_manager.read()
            print 'after read'
            if info['type'] == 'INIT':
                self.unum = info['unum']
                self.side = info['side']
            elif info['type'] == 'BODY':
                self.body_info = info
            elif info['type'] == 'AURAL':
                self.aural_info = info
            elif info['type'] == 'VISION':
                self.vision_info = info
            if (not self.body_info) or (not self.vision_info):
                # received info is not complete, continue to read
                continue

            # agent make a plan according info received
            self.plan()
            # Send plan(commands) to server
            self.msg_manager.send(self.cmds)

            # clear received info and plan
            self.body_info = None
            self.vision_info = None
            self.cmds = []


    # Do extra plan
    def plan(self):
        self.move(-20, -20)

    def dash(self, power, direction = 0):
        cmd = '(dash {0} {1})'.format(power, direction)
        self.cmds.append(cmd)

    def kick(self, power, direction = 0):
        cmd = '(kick {0} {1})'.format(power, direction)
        self.cmds.append(cmd)

    def move(self, x, y):
        cmd = '(move {0} {1})'.format(x, y)
        self.cmds.append(cmd)

    def pointto(self, distance, direction):
        cmd = '(pointto {0} {1})'.format(distance, direction)
        self.cmds.append(cmd)
