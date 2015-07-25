import argparse

SR_FILE_NAMES = {
  'FOOD_GROUP': 'FD_GROUP.txt',
  'DATA_SOURCE': 'DATA_SRC.txt',
  'DERIVATION_CODE': 'DERIV_CD.txt',
  'FOOD_DESCRIPTION': 'FOOD_DES.txt',
  'LANGUAGE_DESCRIPTION': 'LANGDESC.txt',
  'NUTRIENT_DEFINITION': 'NUTR_DEF.txt',
  'SOURCE_CODE': 'SRC_CD.txt',
  'DATA_SOURCE_LINK': 'DATASRCLN.txt',
  'FOOD_GROUP': 'FD_GROUP.txt',
  'FOOTNOTE': 'FOOTNOTE.txt',
  'LANGUAL': 'LANGUAL.txt',
  'NUTRIENT_DATA': 'NUT_DATA.txt',
  'WEIGHT': 'WEIGHT.txt',
}
STRING_DELIMETER = '~'
FIELD_DELIMETER = '^'

parser = argparse.ArgumentParser(description='Parser for the USDA SR DB')
parser.add_argument('sr_dir', help='directory of SR DB files')
parser.add_argument('out_file', help='output file name')
args = parser.parse_args()
