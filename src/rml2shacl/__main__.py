import sys 
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import argparse
import logging
import time
from .RMLtoShacl import RMLtoSHACL

if __name__ == "__main__":
    
    RtoS = RMLtoSHACL()
    parser = argparse.ArgumentParser()
    parser.add_argument("--MAPPING_PATH", "-i", type=str, help="RML mapping file to be converted into SHACL shapes.")
    parser.add_argument("--SHACL_PATH", "-o", type=str,help="Output path for the SHACL shapes")
    parser.add_argument("--LOG_LEVEL", "-l", type=str, default="INFO", help="Logging level of this script")

    args = parser.parse_args()

    loglevel = args.LOG_LEVEL
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
    logging.basicConfig(level=numeric_level)

    start = time.time()
    if args.MAPPING_PATH is None:
        exit()
    else:
        if args.SHACL_PATH is not None:
            RtoS.evaluate_file(args.MAPPING_PATH, args.SHACL_PATH)
        else:
            RtoS.evaluate_file(args.MAPPING_PATH)

    end = time.time()

    print(f"Elapsed time: {end - start} seconds")
