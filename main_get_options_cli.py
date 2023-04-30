#!/home/SRV-CFG/venv-python39/bin/python
#
# Filename: "main_get_options_cli_test.py"
#

# --- local modules ---
#import get_options_cli_getopt.get_options_cli as _goc
import get_options_cli_argparse.get_options_cli as _goc
import common_vars as _cv

if __name__ == "__main__":
    _goc.get_options()
    print(_cv.OPTIONS)

