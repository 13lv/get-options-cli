#
# Filename: "get_options_cli.py"
#
import os
import sys
import getopt
import re
# --- local modules ---
import help
import config as _cfg
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
#       <program use option>: <short options> <long options>
        '1': ('a:b:c:', ['--along=', '--blong=', '--clong=']),
        '2': ('d:e:f:', ['--dlong=', '--elong=', '--flong=']),
    }


    def read_opt(param, param_long):
        try:
            opts, args = getopt.getopt(sys.argv[1:], param, param_long)
        except getopt.GetoptError as e:
            _log.exception(f"got EXCEPTION: \"{e}\"")
            help.help()
            sys.exit(1)
        else:
            return opts, args

    for _, v in allow_opt.items():
        opts, args = read_opt(v[0], v[1])

        if not opts and not args:
            _log.error("Options and Arguments Not Found!")
            help.help()
            sys.exit(1)
        else:
            break

    if args:
        _log.error(f"Arguments Found.")
        help.help()
        sys.exit(1)

    for o, ov in opts:
        _log.info(f"Option: \"{o}\", Option Value: \"{ov}\","
                  f" Options: \"{opts}\", Arguments: \"{args}\"")

        _cfg.OPTIONS[allow_opt_values.get(o, help.help())[0]] = ov

    return _cfg.OPTIONS

