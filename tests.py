import unittest
from row_funcs import RowParser

class RowFuncTest(unittest.TestCase):
  row_parser = RowParser()

  def test_food_group(self):
    code = '0100'
    description = 'Dairy and Egg Products'
    food_group = self.row_parser.food_group([code, description])
    self.assertEqual(food_group.code, code)
    self.assertEqual(food_group.description, description)

  def test_nutrient_definition(self):
    nutrient_number = '203'
    units = 'g'
    tag_name = 'PROCNT'
    nutrient_description = 'Protein'
    num_decimals = '2'
    sr_order = '600'
    nutrient_definition = self.row_parser.nutrient_definition([nutrient_number,
      units, tag_name, nutrient_description, num_decimals, sr_order])
    self.assertEqual(nutrient_definition.nutrient_number, nutrient_number)
    self.assertEqual(nutrient_definition.units, units)
    self.assertEqual(nutrient_definition.tag_name, tag_name)
    self.assertEqual(nutrient_definition.nutrient_description,
      nutrient_description)
    self.assertEqual(nutrient_definition.num_decimals, num_decimals)
    self.assertEqual(nutrient_definition.sr_order, int(sr_order))

  def test_food_description(self):
    ndb_number = '01001'
    food_group_code = '0100'
    food_group_id = 1
    long_description = 'Butter, salted'
    short_description= 'BUTTER, WITH SALT'
    common_name = ''
    manufacturer_name = ''
    survey = 'Y'
    refuse_description = ''
    refuse_percent = '0'
    scientific_name = ''
    nitrogen_factor = '6.38'
    protein_factor = '4.27'
    fat_factor = '8.79'
    carb_factor = '3.87'
    self.row_parser.food_group_code_map[food_group_code] = food_group_id
    food_description = self.row_parser.food_description([ndb_number,
      food_group_code, long_description, short_description, common_name,
      manufacturer_name, survey, refuse_description, refuse_percent,
      scientific_name, nitrogen_factor, protein_factor, fat_factor,
      carb_factor])
    self.assertEqual(food_description.ndb_number, ndb_number)
    self.assertEqual(food_description.food_group_code, food_group_code)
    self.assertEqual(food_description.food_group_id, food_group_id)
    self.assertEqual(food_description.long_description, long_description)
    self.assertEqual(food_description.short_description, short_description)
    self.assertEqual(food_description.common_name, None)
    self.assertEqual(food_description.manufacturer_name, None)
    self.assertEqual(food_description.survey, survey)
    self.assertEqual(food_description.refuse_description, None)
    self.assertEqual(food_description.refuse_percent, int(refuse_percent))
    self.assertEqual(food_description.scientific_name, None)
    self.assertEqual(food_description.nitrogen_factor, float(nitrogen_factor))
    self.assertEqual(food_description.protein_factor, float(protein_factor))
    self.assertEqual(food_description.fat_factor, float(fat_factor))
    self.assertEqual(food_description.carb_factor, float(carb_factor))

  def test_langual(self):
    ndb_number = '02001'
    food_description_id = 2
    factor_code = 'A0113'
    langual_factor_id = 3
    self.row_parser.food_description_ndb_number_map = {
      ndb_number: food_description_id
    }
    self.row_parser.langual_factor_code_map = {
      factor_code: langual_factor_id
    }
    langual = self.row_parser.langual([ndb_number, factor_code])
    self.assertEqual(langual.ndb_number, ndb_number)
    self.assertEqual(langual.food_description_id, food_description_id)
    self.assertEqual(langual.factor_code, factor_code)
    self.assertEqual(langual.langual_factor_id, langual_factor_id)

  def test_langual_factor(self):
    factor_code = 'A0107'
    description = 'BAKERY PRODUCT, UNSWEETENED (US CFR)'
    langual_factor = self.row_parser.langual_factor([factor_code, description])
    self.assertEqual(langual_factor.factor_code, factor_code)
    self.assertEqual(langual_factor.description, description)

  def test_source_code(self):
    code = '1'
    description = 'Analytical or derived from analytical'
    source_code = self.row_parser.source_code([code, description])
    self.assertEqual(source_code.code, code)
    self.assertEqual(source_code.description, description)

  def test_derivation_code(self):
    code = 'A'
    description = 'Analytical data'
    derivation_code = self.row_parser.derivation_code([code, description])
    self.assertEqual(derivation_code.code, code)
    self.assertEqual(derivation_code.description, description)

  def test_nutrient_data(self):
    ndb_number = '01001'
    food_description_id = 1
    nutrient_number = '203'
    nutrient_definition_id = 3
    nutrient_value = '0.85'
    num_data_points = '16'
    standard_error = '0.074'
    source_code_code = '1'
    source_code_id = 1
    derivation_code_code = ''
    reference_ndb_number = ''
    fortified = ''
    num_studies = ''
    min_value = ''
    max_value = ''
    degrees_of_freedom = ''
    low_error_bound = ''
    upper_error_bound = ''
    stat_comments = ''
    last_modified = '11/1976'
    confidence_code = ''
    self.row_parser.food_description_ndb_number_map = {
      ndb_number: food_description_id
    }
    self.row_parser.nutrient_definition_nutrient_number_map = {
      nutrient_number: nutrient_definition_id
    }
    self.row_parser.source_code_code_map = {
      source_code_code: source_code_id
    }
    nutrient_data = self.row_parser.nutrient_data([ndb_number, nutrient_number,
      nutrient_value, num_data_points, standard_error, source_code_code,
      derivation_code_code, reference_ndb_number, fortified, num_studies,
      min_value, max_value, degrees_of_freedom, low_error_bound,
      upper_error_bound, stat_comments, last_modified, confidence_code])
    self.assertEqual(nutrient_data.ndb_number, ndb_number)
    self.assertEqual(nutrient_data.food_description_id, food_description_id)
    self.assertEqual(nutrient_data.nutrient_number, nutrient_number)
    self.assertEqual(nutrient_data.nutrient_definition_id,
      nutrient_definition_id)
    self.assertEqual(nutrient_data.nutrient_value, float(nutrient_value))
    self.assertEqual(nutrient_data.num_data_points, int(num_data_points))
    self.assertEqual(nutrient_data.standard_error, float(standard_error))
    self.assertEqual(nutrient_data.source_code_code, source_code_code)
    self.assertEqual(nutrient_data.source_code_id, source_code_id)
    self.assertEqual(nutrient_data.derivation_code_code, None)
    self.assertEqual(nutrient_data.derivation_code_id, None)
    self.assertEqual(nutrient_data.reference_ndb_number, None)
    self.assertEqual(nutrient_data.reference_food_description_id, None)
    self.assertEqual(nutrient_data.fortified, None)
    self.assertEqual(nutrient_data.num_studies, None)
    self.assertEqual(nutrient_data.min_value, None)
    self.assertEqual(nutrient_data.max_value, None)
    self.assertEqual(nutrient_data.degrees_of_freedom, None)
    self.assertEqual(nutrient_data.low_error_bound, None)
    self.assertEqual(nutrient_data.upper_error_bound, None)
    self.assertEqual(nutrient_data.stat_comments, None)
    self.assertEqual(nutrient_data.last_modified, last_modified)
    self.assertEqual(nutrient_data.confidence_code, None)

  def test_weight(self):
    ndb_number = '01001'
    food_description_id = 1
    sequence_number = '1'
    amount = '1'
    measure_description = 'pat (1" sq, 1/3" high)'
    gram_weight = '5'
    num_data_points = ''
    standard_deviation = ''
    self.row_parser.food_description_ndb_number_map = {
      ndb_number: food_description_id
    }
    weight = self.row_parser.weight([ndb_number, sequence_number, amount,
      measure_description, gram_weight, num_data_points, standard_deviation])
    self.assertEqual(weight.ndb_number, ndb_number)
    self.assertEqual(weight.food_description_id, food_description_id)
    self.assertEqual(weight.sequence_number, sequence_number)
    self.assertEqual(weight.amount, float(amount))
    self.assertEqual(weight.measure_description, measure_description)
    self.assertEqual(weight.gram_weight, float(gram_weight))
    self.assertEqual(weight.num_data_points, None)
    self.assertEqual(weight.standard_deviation, None)

  def test_footnote(self):
    ndb_number = '02009'
    food_description_id = 9
    footnote_number = '01'
    footnote_type = 'D'
    nutrient_number = ''
    footnote_text = 'Mix of chili pepper, other spices and salt'
    self.row_parser.food_description_ndb_number_map = {
      ndb_number: food_description_id
    }
    footnote = self.row_parser.footnote([ndb_number, footnote_number,
      footnote_type, nutrient_number, footnote_text])
    self.assertEqual(footnote.ndb_number, ndb_number)
    self.assertEqual(footnote.food_description_id, food_description_id)
    self.assertEqual(footnote.footnote_number, footnote_number)
    self.assertEqual(footnote.footnote_type, footnote_type)
    self.assertEqual(footnote.nutrient_number, None)
    self.assertEqual(footnote.footnote_text, footnote_text)

  def test_data_source(self):
    data_source_id = 'D1066'
    authors = 'G.V. Mann'
    title = 'The Health and Nutritional status of Alaskan Eskimos.'
    year = '1962'
    journal = 'American Journal of Clinical Nutrition'
    volume_city = '11'
    issue_state = ''
    start_page = '31'
    end_page = '76'
    data_source = self.row_parser.data_source([data_source_id, authors, title, year,
      journal, volume_city, issue_state, start_page, end_page])
    print data_source.id
    self.assertEqual(data_source.data_source_id, data_source_id)
    self.assertEqual(data_source.authors, authors)
    self.assertEqual(data_source.title, title)
    self.assertEqual(data_source.year, year)
    self.assertEqual(data_source.journal, journal)
    self.assertEqual(data_source.volume_city, volume_city)
    self.assertEqual(data_source.issue_state, None)
    self.assertEqual(data_source.start_page, start_page)
    self.assertEqual(data_source.end_page, end_page)

  def test_data_source_link(self):
    ndb_number = '10984'
    food_description_id = 84
    nutrient_number = '518'
    nutrient_definition_id = 18
    data_source_id_id = 'S3941'
    data_source_id = 41
    self.row_parser.food_description_ndb_number_map = {
      ndb_number: food_description_id
    }
    self.row_parser.nutrient_definition_nutrient_number_map = {
      nutrient_number: nutrient_definition_id
    }
    self.row_parser.data_source_id_id_map = {
      data_source_id_id: data_source_id
    }
    data_source_link = self.row_parser.data_source_link([ndb_number,
      nutrient_number, data_source_id_id])
    self.assertEqual(data_source_link.ndb_number, ndb_number)
    self.assertEqual(data_source_link.food_description_id, food_description_id)
    self.assertEqual(data_source_link.nutrient_number, nutrient_number)
    self.assertEqual(data_source_link.nutrient_definition_id,
      nutrient_definition_id)
    self.assertEqual(data_source_link.data_source_id_id, data_source_id_id)
    self.assertEqual(data_source_link.data_source_id, data_source_id)

if __name__ == '__main__':
  unittest.main()
