#
# Filename: "help.py"
#
import sys

def help(hid=''):
    help_map = {
        'help_1': ("\n --- <Description 1> ---"
f"\n Usage: {sys.argv[0]} [-a <> ()] [-b <> ()] [-c <> ()]\n"
        ),

        'help_2': ("\n --- <Description 2> ---"
f"\n Usage: {sys.argv[0]} [-d <> ()] [-e <> ()] [-f <> ()]\n"
        ),
    }

    help_str= help_map.get(f"help_{hid}")
    if not help_str is None:
        print(help_str)
    else:
        for _, v in help_map.items():
            print(v)

