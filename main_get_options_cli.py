#!/home/SRV-CFG/venv-python39/bin/python
#
# Filename: "main_get_options_cli_test.py"
#

# --- local modules ---
import get_options_cli as _goc
import config as _cfg

if __name__ == "__main__":
    _goc.get_options()
    print(_cfg.OPTIONS)

