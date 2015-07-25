import argparse

parser = argparse.ArgumentParser(description='Parser for the USDA SR DB')
parser.add_argument('sr_dir', help='directory of SR DB files')
parser.add_argument('out_file', help='output file name')
args = parser.parse_args()
