#
# Filename: "logger.py"
#
import os
import sys
import datetime as _dt
# --- local modules ---
import common_simple as _cmns


class Logger():
    def __init__(self, fname=os.path.basename(__file__).split(".")[0]):
        self.fname = fname

    def _print_log(self, level, nstr, msg, dnl=True):
        """
        dnl -> disable new line
        """
        def rm_nl(msg):
            if _cmns.is_true(dnl):
                return ' '.join(msg.split())
            return msg

        print(f" -> {_dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}"
f":{level}:{self.fname}:{nstr} %(msg)s"%{'msg': rm_nl(msg)})

    def info(self, msg):
        self._print_log('INFO', sys._getframe().f_back.f_lineno, msg)

    def error(self, msg):
        self._print_log('ERROR', sys._getframe().f_back.f_lineno, msg)

    def exception(self,msg, dnl=True):
        """
        dnl -> disable new line
        """
        self._print_log('ERROR', sys._getframe().f_back.f_lineno, msg, dnl)

