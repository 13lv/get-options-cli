#
# Filename: "get_options_cli.py"
#
import argparse
# --- local modules ---

def get_options():
    """
    function input parameters:
    function output parameters:
    """
    parser = argparse.ArgumentParser(prog='ast-cdr-mgmt', 
                description='*** <Description for Programm \"%(prog)S\"> ***',
                epilog= 'Thanks for using \"%(prog)s\"! :)')

    parser.add_argument('arg_1', type=str, 
            default='arg_arg_1', help='Test help arg_1')

    parser.add_argument('-a', '--along', nargs=2, metavar=('A', 'B'), 
    required=True, type=str, default="<opt_a_dflt>", 
    help='Test help a \"%(metavar)s\"')

    parser.add_argument('-b', '--blong', metavar='', type=str, 
        choices=['b1', 'b2'], default="<opt_b_dflt>", help='Test help b')

    parser.add_argument('-c', '--clong', metavar='', type=str, 
            default="<opt_c_dflt>", help='Test help c')

    args = parser.parse_args()

    print(args)
