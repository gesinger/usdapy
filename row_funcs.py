from models import FoodGroup, NutrientDefinition, FoodDescription, Langual, \
  LangualFactor, SourceCode, DerivationCode, NutrientData, Weight, Footnote, \
  DataSource, DataSourceLink

class RowParser:
  food_group_code_map = {}
  food_description_ndb_number_map = {}
  langual_factor_code_map = {}
  nutrient_definition_nutrient_number_map = {}
  source_code_code_map = {}
  derivation_code_code_map = {}
  data_source_id_id_map = {}

  def food_group(self, fields):
    return FoodGroup(code=fields[0], description=fields[1])

  def nutrient_definition(self, fields):
    return NutrientDefinition(nutrient_number=fields[0], units=fields[1],
      tag_name=fields[2] or None, nutrient_description=fields[3],
      num_decimals=fields[4], sr_order=int(fields[5]))

  def food_description(self, fields):
    food_description = FoodDescription(ndb_number=fields[0],
      food_group_code=fields[1], long_description=fields[2],
      short_description=fields[3], common_name=fields[4] or None,
      manufacturer_name=fields[5] or None, survey=fields[6] or None,
      refuse_description=fields[7] or None,
      refuse_percent=int(fields[8]) if fields[8] else None,
      scientific_name=fields[9] or None,
      nitrogen_factor=float(fields[10]) if fields[10] else None,
      protein_factor=float(fields[11]) if fields[11] else None,
      fat_factor=float(fields[12]) if fields[12] else None,
      carb_factor=float(fields[13]) if fields[13] else None)
    food_description.food_group_id = \
      self.food_group_code_map[food_description.food_group_code]
    return food_description

  def langual(self, fields):
    langual = Langual(ndb_number=fields[0], factor_code=fields[1])
    langual.food_description_id = \
      self.food_description_ndb_number_map[langual.ndb_number]
    langual.langual_factor_id = \
      self.langual_factor_code_map[langual.factor_code]
    return langual

  def langual_factor(self, fields):
    return LangualFactor(factor_code=fields[0], description=fields[1])

  def source_code(self, fields):
    return SourceCode(code=fields[0], description=fields[1])

  def derivation_code(self, fields):
    return DerivationCode(code=fields[0], description=fields[1])

  def nutrient_data(self, fields):
    nutrient_data = NutrientData(ndb_number=fields[0], nutrient_number=fields[1],
      nutrient_value=float(fields[2]), num_data_points=int(fields[3]),
      standard_error=float(fields[4]) if fields[4] else None,
      source_code_code=fields[5], derivation_code_code=fields[6] or None,
      reference_ndb_number=fields[7] or None, fortified=fields[8] or None,
      num_studies=int(fields[9]) if fields[9] else None,
      min_value=float(fields[10]) if fields[10] else None,
      max_value=float(fields[11]) if fields[11] else None,
      degrees_of_freedom=int(fields[12]) if fields[12] else None,
      low_error_bound=float(fields[13]) if fields[13] else None,
      upper_error_bound=float(fields[14]) if fields[14] else None,
      stat_comments=fields[15] or None, last_modified=fields[16] or None,
      confidence_code=fields[17] or None)
    nutrient_data.food_description_id = \
      self.food_description_ndb_number_map[nutrient_data.ndb_number]
    nutrient_data.nutrient_definition_id = \
      self.nutrient_definition_nutrient_number_map[nutrient_data.nutrient_number]
    nutrient_data.source_code_id = \
      self.source_code_code_map[nutrient_data.source_code_code]
    if nutrient_data.derivation_code_code:
      nutrient_data.derivation_code_id = \
        self.derivation_code_code_map[nutrient_data.derivation_code_code]
    if nutrient_data.reference_ndb_number:
      nutrient_data.reference_food_description_id = \
        self.food_description_ndb_number_map[nutrient_data.reference_ndb_number]
    return nutrient_data

  def weight(self, fields):
    weight = Weight(ndb_number=fields[0], sequence_number=fields[1],
      amount=float(fields[2]), measure_description=fields[3],
      gram_weight=float(fields[4]),
      num_data_points=int(fields[5]) if fields[5] else None,
      standard_deviation=float(fields[6]) if fields[6] else None)
    weight.food_description_id = \
      self.food_description_ndb_number_map[weight.ndb_number]
    return weight

  def footnote(self, fields):
    footnote = Footnote(ndb_number=fields[0], footnote_number=fields[1],
      footnote_type=fields[2], nutrient_number=fields[3] or None,
      footnote_text=fields[4])
    footnote.food_description_id = \
      self.food_description_ndb_number_map[footnote.ndb_number]
    if footnote.nutrient_number:
      footnote.nutrient_definition_id = \
        self.nutrient_definition_nutrient_number_map[footnote.nutrient_number]
    return footnote

  def data_source(self, fields):
    return DataSource(data_source_id=fields[0], authors=fields[1] or None,
      title=fields[2], year=fields[3] or None, journal=fields[4] or None,
      volume_city=fields[5] or None, issue_state=fields[6] or None,
      start_page=fields[7] or None, end_page=fields[8] or None)

  def data_source_link(self, fields):
    data_source_link = DataSourceLink(ndb_number=fields[0],
      nutrient_number=fields[1], data_source_id_id=fields[2])
    data_source_link.food_description_id = \
      self.food_description_ndb_number_map[data_source_link.ndb_number]
    data_source_link.nutrient_definition_id = \
      self.nutrient_definition_nutrient_number_map[data_source_link.nutrient_number]
    data_source_link.data_source_id = \
      self.data_source_id_id_map[data_source_link.data_source_id_id]
    return data_source_link
