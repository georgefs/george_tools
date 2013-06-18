#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2013 george
#
# Distributed under terms of the MIT license.

import os
import datetime


def at(time, script):

    assert isinstance(time, (str, datetime.timedelta)), 'time type error'
    assert isinstance(script, str), 'script type error'

    if isinstance(time, datetime.timedelta):
        time = " now + {} minutes ".format(int(time.total_seconds() / 60))

    command_template = """
    at {}<<EOF
    {}
    EOF
    """

    command = command_template.format(time, script)

    i, o = os.popen4(command)
    return o


if __name__ == '__main__':
    import uuid
    import time

    name = str(uuid.uuid1())
    at('now', 'echo test > /tmp/{}'.format(name))
    time.sleep(2)
    i, o = os.popen4('cat /tmp/{}'.format(name))

    assert o.read() == 'test\n', 'test error'

    os.popen('rm /tmp/{}'.format(name))
