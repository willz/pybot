import re
import utils

class Parser:
    def parse(self, msg):
        flag = msg[1:5]
        if flag == 'init':
            return self.parse_init(msg)
        elif flag == 'sens':
            return self.parse_body(msg)
        elif flag == 'see ':
            return self.parse_vision(msg)
        else:
            print 'msg', msg
        
    def parse_init(self, msg):
        m = re.match(r'\(init ([lr]) (\d+) (\w+)', msg)
        side, unum, mode = m.groups()
        info = {'type': 'INIT', 'side': side, 'unum': unum, 'mode': mode}
        utils.int_dict(info)
        return info

    def parse_body(self, msg):
        info = {'type': 'BODY'}
        print msg
        m = re.match(r'.*view_mode (\w+) (\w+)', msg)
        info['view_mode'] = m.groups()
        m = re.match(r'.*stamina (\d+) (\d+)', msg)
        info['stamina'] = m.group(0)
        info['effort'] = m.group(1)
        m = re.match(r'.*speed (\d+)', msg)
        info['speed'] = m.group(0)

        attrs = ['kick', 'dash', 'turn', 'say', 'turn_neck', 'catch', 'move',
                 'change_view']
        for attr in attrs:
            pat = '.*{0} (\d+)'.format(attr)
            m = re.match(pat, msg)
            info[attr] = m.groups(0)

        utils.int_dict(info)
        return info

    def parse_vision(self, msg):
        info = {'type': 'VISION'}
        utils.int_dict(info)
        return info


