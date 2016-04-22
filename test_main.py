# -*- coding: utf-8 -*-
#!/usr/bin/python
import tsl2591

if __name__ == "__main__":
    while state <= 1 and state >= 0:
        if get_bumper() == 1:
            if state == 0:
                straight()
                state = 1
                

