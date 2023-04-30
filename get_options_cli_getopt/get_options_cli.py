#
# Filename: "get_options_cli.py"
#
import os
import sys
import getopt
import re
# --- local modules ---
import get_options_cli_getopt.help
import common_vars as _cv
import logger as _lggr

fname = os.path.basename(__file__).split(".")[0] # название текущего файла.

_log = _lggr.Logger(fname)


def _get_options():
    """
    function input parameters:
    function output parameters:
    """
    allow_opts_values = {
#       <short option>: (<variable name>, <regex option value>)

        '-a': ('a_var', r'^[A-z]{3,255}$'),
        '--along': ('along_var', r'^[A-z]{7,255}$'),
        '-b': ('b_var', r'^[A-z]{3,255}$'),
        '--blong': ('blong_var', r'^[A-z]{7,255}$'),
        '-c': ('c_var', r'^[A-z]{3,255}$'),
        '--clong': ('clong_var', r'^[A-z]{7,255}$'),

        '-d': ('d_var', r'^[A-z]{3,255}$'),
        '--dlong': ('dlong_var', r'^[A-z]{7,255}$'),
        '-e': ('e_var', r'^[A-z]{3,255}$'),
        '--elong': ('elong_var', r'^[A-z]{7,255}$'),
        '-f': ('f_var', r'^[A-z]{3,255}$'),
        '--flong': ('flong_var', r'^[A-z]{7,255}$'),
    }

    allow_opts = {
#       <program use option>: <short options> <long options>
        '1': ('a:b:c:', ['along=', 'blong=', 'clong=']),
        '2': ('d:e:f:', ['dlong=', 'elong=', 'flong=']),
    }

    allow_args = (
        'ppp',
    )

    def read_opt_arg(param, param_long):
        print(param, param_long) # Test
        try:
            opts, args = getopt.getopt(sys.argv[1:], param, param_long)
        except getopt.GetoptError as e:
            _log.exception(f"got EXCEPTION: \"{e}\"")
            help.help()
            sys.exit(1)
        else:
            return opts, args

    for k, v in allow_opts.items():
        print(k,v) # Test
        opts, args = read_opt_arg(v[0], v[1])

        if not opts and not args:
            _log.error("Options and Arguments Not Found!")
            help.help()
            sys.exit(1)
        else:
            break

    for a in args:
        _log.info(f"Argumen: \"{a}\", Arguments: \"{args}\"")
        if not a in allow_args:
            _log.error(f"Found Not allower argument.")
            help.help()
            sys.exit(1)

    def chk_arg(opt='', val=''):
        ptrn_arg = re.compile(allow_opts_values.get(opt, ('', ''))[1])
        if ptrn_arg.match(val) is None:
            _log.error(f"Option: \"{opt}\" has No Acceptable value \"{val}\"!")
            help.help()
            sys.exit(1)

    for o, ov in opts:
        _log.info(f"Option: \"{o}\", Option Value: \"{ov}\","
                  f" Options: \"{opts}\"")

        chk_arg(o, ov)

        _cv.OPTIONS[allow_opts_values.get(o)[0]] = ov

    return _cfg.OPTIONS


# Test
def get_options():
#    _get_options()
    opts, args = getopt.getopt(sys.argv[1:], 'a:bc:', ['along=', 'blong=', 'clong='])
    print(f"Options: \"{opts}\", Arguments: \"{args}\"")

