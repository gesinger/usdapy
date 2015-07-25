from models import FoodGroup, NutrientDefinition, FoodDescription, Langual, \
  LangualFactor, SourceCode, DerivationCode, NutrientData, Weight, Footnote, \
  DataSource, DataSourceLink

def food_group(fields):
  return FoodGroup(code=fields[0], description=fields[1])

def nutrient_definition(fields):
  return NutrientDefinition(nutrient_number=fields[0], units=fields[1],
    tag_name=fields[2] or None, nutrient_description=fields[3],
    num_decimals=fields[4], sr_order=int(fields[5]))

def food_description(fields):
  return FoodDescription(ndb_number=fields[0], food_group_code=fields[1],
    long_description=fields[2], short_description=fields[3],
    common_name=fields[4] or None, manufacturer_name=fields[5] or None,
    survey=fields[6] or None, refuse_description=fields[7] or None,
    refuse_percent=int(fields[8]) if fields[8] else None,
    scientific_name=fields[9] or None,
    nitrogen_factor=float(fields[10]) if fields[10] else None,
    protein_factor=float(fields[11]) if fields[11] else None,
    fat_factor=float(fields[12]) if fields[12] else None,
    carb_factor=float(fields[13]) if fields[13] else None)

def langual(fields):
  return Langual(ndb_number=fields[0], factor_code=fields[1])

def langual_factor(fields):
  return LangualFactor(factor_code=fields[0], description=fields[1])

def source_code(fields):
  return SourceCode(code=fields[0], description=fields[1])

def derivation_code(fields):
  return DerivationCode(code=fields[0], description=fields[1])

def nutrient_data(fields):
  return NutrientData(ndb_number=fields[0], nutrient_number=fields[1],
    nutrient_value=float(fields[2]), num_data_points=int(fields[3]),
    standard_error=float(fields[4]) if fields[4] else None,
    source_code=fields[5], derivation_code=fields[6] or None,
    reference_ndb_number=fields[7] or None, fortified=fields[8] or None,
    num_studies=int(fields[9]) if fields[9] else None,
    min_value=float(fields[10]) if fields[10] else None,
    max_value=float(fields[11]) if fields[11] else None,
    degrees_of_freedom=int(fields[12]) if fields[12] else None,
    low_error_bound=float(fields[13]) if fields[13] else None,
    upper_error_bound=float(fields[14]) if fields[14] else None,
    stat_comments=fields[15] or None, last_modified=fields[16] or None,
    confidence_code=fields[17] or None)

def weight(fields):
  return Weight(ndb_number=fields[0], sequence_number=fields[1],
    amount=float(fields[2]), measure_description=fields[3],
    gram_weight=float(fields[4]),
    num_data_points=int(fields[5]) if fields[5] else None,
    standard_deviation=float(fields[6]) if fields[6] else None)

def footnote(fields):
  return Footnote(ndb_number=fields[0], footnote_number=fields[1],
    footnote_type=fields[2], nutrient_number=fields[3] or None,
    footnote_text=fields[4])

def data_source(fields):
  return DataSource(id=fields[0], authors=fields[1] or None, title=fields[2],
    year=fields[3] or None, journal=fields[4] or None,
    volume_city=fields[5] or None, issue_state=fields[6] or None,
    start_page=fields[7] or None, end_page=fields[8] or None)

def data_source_link(fields):
  return DataSourceLink(ndb_number=fields[0], nutrient_number=fields[1],
    data_source_id=fields[2])
