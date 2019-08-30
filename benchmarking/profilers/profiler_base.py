#!/usr/bin/env python

##############################################################################
# Copyright 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
##############################################################################

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import abc

from utils.future import Future


class ProfilerBase(object):
    def __init__(self, id=None):
        self.id = id

    def start(self):
        f = Future(self._start)
        f.start(self.id)
        return f

    @abc.abstractmethod
    def _start(self, id):
        return None

    def getId(self, f):
        return f.result()
