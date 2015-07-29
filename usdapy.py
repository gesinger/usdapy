import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, FoodGroup, NutrientDefinition, FoodDescription, \
  LangualFactor, SourceCode, DerivationCode, DataSource
from row_funcs import RowParser
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

row_parser = RowParser()

parse('FD_GROUP.txt', row_parser.food_group)
row_parser.food_group_code_map = {food_group.code: food_group.id for \
  food_group in session.query(FoodGroup.id, FoodGroup.code).all()}
parse('NUTR_DEF.txt', row_parser.nutrient_definition)
row_parser.nutrient_definition_nutrient_number_map = {
  nutrient_definition.nutrient_number: nutrient_definition.id for \
  nutrient_definition in session.query(
  NutrientDefinition.id, NutrientDefinition.nutrient_number).all()}
parse('FOOD_DES.txt', row_parser.food_description)
row_parser.food_description_ndb_number_map = {
  food_description.ndb_number: food_description.id for food_description in \
  session.query(FoodDescription.id, FoodDescription.ndb_number).all()}
parse('LANGDESC.txt', row_parser.langual_factor)
row_parser.langual_factor_code_map = {
  langual_factor.factor_code: langual_factor.id for langual_factor in \
  session.query(LangualFactor.id, LangualFactor.factor_code).all()}
parse('LANGUAL.txt', row_parser.langual)
parse('SRC_CD.txt', row_parser.source_code)
row_parser.source_code_code_map = {
  source_code.code: source_code.id for source_code in session.query(
  SourceCode.id, SourceCode.code).all()}
parse('DERIV_CD.txt', row_parser.derivation_code)
row_parser.derivation_code_code_map = {
  derivation_code.code: derivation_code.id for derivation_code in \
  session.query(DerivationCode.id, DerivationCode.code).all()}
parse('NUT_DATA.txt', row_parser.nutrient_data)
parse('WEIGHT.txt', row_parser.weight)
parse('FOOTNOTE.txt', row_parser.footnote)
parse('DATA_SRC.txt', row_parser.data_source)
row_parser.data_source_id_id_map = {
  data_source.data_source_id: data_source.id for data_source in \
  session.query(DataSource.id, DataSource.data_source_id).all()}
parse('DATSRCLN.txt', row_parser.data_source_link)
