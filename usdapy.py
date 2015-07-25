import argparse

parser = argparse.ArgumentParser(description='Parser for the USDA SR DB')
parser.add_argument('srdir', help='directory of SR DB files')
args = parser.parse_args()
