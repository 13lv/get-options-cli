#
# Filename: "get_options_cli.py"
#
import sys
import argparse
from gettext import gettext
# --- local modules ---


#parser = argparse.ArgumentParser(prog='ast-cdr-mgmt',
#                description='--- <Description for Programm \"%(prog)s\"> ---',
#                epilog= 'Thanks for using \"%(prog)s\"! :)')
#
#parser.add_argument('arg_1', type=str, default='arg_arg_1',
#        help='Test help arg_1')
#
#parser.add_argument('-a', '--along', dest='a_var', nargs=2, metavar=('A', 'B'),
#        required=True, type=str, default="<opt_a_dflt>",
#        help='Test help a \"%(metavar)s\"')
#
#parser.add_argument('-b', '--blong', dest='b_var', metavar='', type=str,
#        choices=['b1', 'b2'], default="<opt_b_dflt>", help='Test help b')
#
#parser.add_argument('-c', '--clong', dest='c_var', metavar='', type=str,
#            default="<opt_c_dflt>", help='Test help c')
#
#args = parser.parse_args()
#
#print(args)


class MyCustomArgParse(argparse.ArgumentParser):
    color_dict = {
        'white': '1;97',

        'dred': '0;31',
        'dgreen': '0;32',
        'dyellow': '0;33',
        'dblue': '0;34',
        'dmagenta': '0;35',
        'dcyan': '0;36',
        'dgray': '1;90',

        'red': '1;91',
        'green': '1;92',
        'yellow': '1;93',
        'blue': '1;94',
        'magenta': '1;95',
        'cyan': '1;96',
        'gray': '0;37',

#        'red': '1;31',
#        'green': '1;32',
#        'yellow': '1;33',
#        'blue': '1;34',
#        'cyan': '1;36',
    }

    def print_usage(self, file=None):
        if file is None:
            file = sys.stdout

        line_usage = self.format_usage()

        color = self.color_dict.get('yellow')
        if not color is None:
            line_usage = '\n \x1b[%sm%s\x1b[0m\n'%(color, 
                f"{line_usage[0].upper()}{line_usage[1:]}")

            if not file is sys.stdout or not file is sys.stderr:
                file = sys.stdout
        else:
            line_usage = '\n %s%s\n'%(line_usage[0].upper(), line_usage[1:])

        self._print_message(line_usage, file)

    def print_help(self, file=None):
        if file is None:
            file = sys.stdout

        help = self.format_help().split('\n')

        color = self.color_dict.get('dgray')
        if not color is None:
            usage_part = (
                '\n\x1b[1;93m ● %s%s\x1b[0m'%(help[0][0].upper(), help[0][1:])
            )
            line_help = "%s\n\x1b[%sm%s%s\x1b[0m"%(usage_part, color, 
                                                '\n '.join(help[1:]), '-'*79)

            if not file is sys.stdout or not file is sys.stderr:
                file = sys.stdout
        else:
            usage_part = (
                '\n ● %s%s'%(help[0][0].upper(), help[0][1:])
            )
            line_help = "%s\n%s"%(usage_part, '\n '.join(help[1:]))

        self._print_message(line_help, file)

    def exit(self, status=0, message=None):
        if message:
            color = self.color_dict.get('dred')
            if not color is None:
                message = (
                    '\x1b[%sm%s\x1b[0m'%(color, message)
                )
            self._print_message(message, sys.stderr)
        sys.exit(status)

    def error(self, message):
        self.print_usage(sys.stderr)
        args = {'prog': self.prog, 'message': message}
        self.exit(2, gettext(' ● \"%(prog)s\" Error: %(message)s\n') % args)


parser = MyCustomArgParse(
#    prog = sys.argv[0],
    prog='ast-cdr-mgmt', 
    description='--- < Description for Programm \"%(prog)s\" > ---',
    epilog= 'Thanks for using \"%(prog)s\"! :)'
)

parser.add_argument('arg_1', 
    type=str, 
    default='arg_arg_1', 
    help='Test help arg_1'
)

parser.add_argument('-a', '--along', dest='a_var', 
    nargs=2, 
    metavar=('A', 'B'), 
    required=True, type=str, default="<opt_a_dflt>", 
    help='Test help a \"%(metavar)s\"'
)

parser.add_argument('-b', '--blong', dest='b_var', 
    metavar='', 
    type=str, 
    choices=['b1', 'b2'], 
    default="<opt_b_dflt>", 
    help='Test help b'
)

parser.add_argument('-c', '--clong', dest='c_var', 
    metavar='', 
    type=str, required=True, 
    default="<opt_c_dflt>", 
    help='Test help c'
)

args = parser.parse_args()

print(args)

