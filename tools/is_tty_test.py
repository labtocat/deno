#!/usr/bin/env python
# Copyright 2018-2019 the Deno authors. All rights reserved. MIT license.
import os
import subprocess
import unittest
from sys import stdin

from util import DenoTestCase, test_main, tty_capture

IS_TTY_TEST_TS = "tests/is_tty.ts"


@unittest.skipIf(os.name == 'nt', "Unable to test tty on Windows")
class TestIsTty(DenoTestCase):
    def test_is_tty(self):
        cmd = [self.deno_exe, "run", IS_TTY_TEST_TS]
        code, stdout, _ = tty_capture(cmd, b'')
        assert code == 0
        assert str(stdin.isatty()).lower() in stdout


if __name__ == "__main__":
    test_main()
