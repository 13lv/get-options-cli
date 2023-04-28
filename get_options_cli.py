#
# Filename: "get_options_cli.py"
#
import os
import sys
import getopt
import re
# --- local modules ---
import help
import logger as _lggr

fname = os.path.basename(__file__).split(".")[0] # название текущего файла.

_log = _lggr.Logger(fname)


def get_options():
    """
    function input parameters:
    function output parameters:
    """
    allow_opt_values = {
#       <short option>: (<variable name>, <regex option value>)

        '-a': ('var_1', r'^[A-z]{10,255}$'),
        '-b': ('var_2', r'^[A-z]{10,255}$'),
        '-c': ('var_3', r'^[A-z]{10,255}$'),

        '-d': ('var_4', r'^[A-z]{10,255}$'),
        '-e': ('var_5', r'^[A-z]{10,255}$'),
        '-f': ('var_6', r'^[A-z]{10,255}$'),
    }

    allow_opt = {
            #       <program use option>: <>
        '1': 'a:b:c:',
        '1L': ['--along=', '--blong=', '--clong='],
        '2': 'd:e:f:',
        '2L': ['--dlong=', '--elong=', '--flong='],

        '': '',
    }


    def read_opt(param, param_long):
        try:
            opts, args = getopt.getopt(sys.argv[1:], param, param_long)
        except getopt.GetoptError:
            help.help()
            sys.exit(1)
        else:
            return opts, args


    opts, args = read_opt(allow_opt['1'], allow_opt['1L'])

    if not opts:
        _log.error(f"Options not Found!")
        help.help()
        sys.exit(1)

    if args:
        _log.error(f"Arguments Found.")
        help.help()
        sys.exit(1)

    options = {}

    for o, ov in opts:
        _log.info()

        options[allow_opt.get(o, help.help())] = ov

    return options

