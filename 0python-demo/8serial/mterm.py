from serial.tools import miniterm
import sys
 
# from .utils import default_port
 
def terminal(port, baud='9600'):
    """Launch minterm from pyserial"""
    testargs = ['nodemcu-uploader', port, baud]
    # TODO: modifying argv is no good
    sys.argv = testargs
    # resuse miniterm on main function
    miniterm.main()

if __name__=="__main__":
    terminal(port="/dev/ttyUSB0", baud=38400)