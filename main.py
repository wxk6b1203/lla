import os
import sys
import time
import argparse


def interface():
    """The command line interface
    :returns: TODO

    """
    print("Latitude and longitude to Address(baidu API)")


def main():
    parser = argparse.ArgumentParser(description="Lati\
            tude and longitude to Address")
    parser.add_argument('-i', '--intereactive', action="store_true",
                        default=False, help="Interactive mode.")
    parser.add_argument('-rt', '--txt', type=str,
                        help="Read from txt(see docs for format)")
    parser.add_argument('-rx', '--xls', type=str, dest="xls",
                        help="Read from xls")
    parser.add_argument('-ox', type=str,
                        help="Write to xls")
    parser.add_argument('-ot', type=str,
                        help="Write to txt")
    parser.add_argument('-a', action="store_true",
                        help="Appending mode(write out only)")
    args = parser.parse_args()
    if args.intereactive is False and args.txt is None and args.xls is None:
        parser.print_help()


if __name__ == '__main__':
    main()
