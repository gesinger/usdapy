import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import row_funcs
import time

STRING_DELIMETER = '~'
FIELD_DELIMETER = '^'

parser = argparse.ArgumentParser(description='Parser for the USDA SR DB')
parser.add_argument('sr_dir', help='directory of SR DB files')
parser.add_argument('out_file', help='output file name')
args = parser.parse_args()

engine = create_engine('sqlite:///{}'.format(args.out_file))
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

def parse(file_name, row_function):
  start_time = time.time()
  with open(args.sr_dir + '/' + file_name) as f:
    for idx, line in enumerate(f):
      fields = line.decode('latin-1').strip().split(FIELD_DELIMETER)
      fields = [field.strip(STRING_DELIMETER) for field in fields]
      row = row_function(fields)
      session.add(row)
      if idx % 1000 == 0:
        session.commit()
  session.commit()
  print "Finished {} in {} seconds".format(file_name, time.time() - start_time)

parse('FD_GROUP.txt', row_funcs.food_group)
parse('NUTR_DEF.txt', row_funcs.nutrient_definition)
parse('FOOD_DES.txt', row_funcs.food_description)
parse('LANGUAL.txt', row_funcs.langual)
parse('LANGDESC.txt', row_funcs.langual_factor)
parse('SRC_CD.txt', row_funcs.source_code)
parse('DERIV_CD.txt', row_funcs.derivation_code)
parse('NUT_DATA.txt', row_funcs.nutrient_data)
parse('WEIGHT.txt', row_funcs.weight)
parse('FOOTNOTE.txt', row_funcs.footnote)
parse('DATA_SRC.txt', row_funcs.data_source)
parse('DATASRCLN', row_funcs.data_source_link)

session.commit()
