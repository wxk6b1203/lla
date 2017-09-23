import os
import sys
import time
import argparse
sys.path.append(os.getcwd() + '/src')
#  import getpos as gp


def interface():
    """The command line interface
    :returns: TODO

    """
    print("Latitude and longitude to Address(baidu API)")


def main():
    import getpos as gp
    inFormat = ""
    inFile = ""
    outFormat = ""
    outFile = ""

    parser = argparse.ArgumentParser(description="Lati\
tude and longitude to Address")
    parser.add_argument('-i', '--intereactive', action="store_true",
                        default=False, help="Interactive mode.\
                                Input 'q' to quick")
    parser.add_argument('-rt', '--txt', type=str,
                        help="Read from txt(see docs for format)")
    parser.add_argument('-rx', '--xls', type=str, dest="xls",
                        help="Read from xls")
    parser.add_argument('-ox', type=str, dest="xlsDest", default="data.xls",
                        help="Write to xls")
    parser.add_argument('-ot', type=str, dest="txtDest",
                        help="Write to txt")
    parser.add_argument('-a', '--append', action="store_true", default=False,
                        help="Appending mode(write out only)")
    parser.add_argument('-v', '--version',
                        action='version',
                        version='LLA(baidu API) v0.1')
    args = parser.parse_args()

    if args.intereactive is False and args.txt is None and args.xls is None:
        parser.print_help()
    elif args.intereactive is True:
        gp.interv()
    else:
        if args.txt is not None:
            inFormat = "txt"
            inFile = args.txt
        elif args.xls is not None:
            inFormat = "xls"
            inFile = args.xls
        if args.txtDest is not None:
            outFormat = "txt"
            outFile = args.txtDest
        else:
            outFormat = "xls"
            outFile = args.xlsDest
    if args.append is True:
        gp.getPos(inFormat, inFile, inFormat, inFile, args.append)
    else:
        gp.getPos(inFormat, inFile, outFormat, outFile, args.append)


if __name__ == '__main__':
    main()
