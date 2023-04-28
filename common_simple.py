#
# Filename: "common_simple.py"
#
# --- local modules ---
#import settings as _stng

def _stng(): # dummy
    pass

_stng.EXECUTE = 'true'

# --- Check True, False
#
def is_true(val='n/a'):
    """
    Checking allowed True values
    function input parameters: Not Set or
    function output parameters: return True if input  or "settings.py"
        parameters in (True, False, 1, 'yes', 'y', 'ok', 'true')
        else return False
    """
    switch = _stng.EXECUTE
    if not val == 'n/a':
        switch = str(val)

    if type(switch) is bool:
        return switch

    if switch.lower() in ('1', 'yes', 'y', 'ok', 'true'):
        return True
    return False

