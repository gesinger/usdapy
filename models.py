from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey, SmallInteger, Numeric, \
  Integer, Index

Base = declarative_base()

class FoodGroup(Base):
  __tablename__ = 'food_groups'

  id = Column(Integer, primary_key=True)
  code = Column(String(4), index=True, unique=True, nullable=False)
  description = Column(String(60), nullable=False)

class NutrientDefinition(Base):
  __tablename__ = 'nutrient_definitions'

  id = Column(Integer, primary_key=True)
  nutrient_number = Column(String(3), index=True, unique=True, nullable=False)
  units = Column(String(7), nullable=False)
  tag_name = Column(String(20), nullable=True)
  nutrient_description = Column(String(60), nullable=False)
  num_decimals = Column(String(1), nullable=False)
  sr_order = Column(Integer, nullable=False)

class FoodDescription(Base):
  __tablename__ = 'food_descriptions'

  id = Column(Integer, primary_key=True)
  ndb_number = Column(String(5), index=True, unique=True, nullable=False)
  food_group_code = Column(String(4), ForeignKey(FoodGroup.code))
  long_description = Column(String(200), nullable=False)
  short_description = Column(String(60), nullable=False)
  common_name = Column(String(100), nullable=True)
  manufacturer_name = Column(String(65), nullable=True)
  survey = Column(String(1), nullable=True)
  refuse_description = Column(String(135), nullable=True)
  refuse_percent = Column(SmallInteger, nullable=True)
  scientific_name = Column(String(65), nullable=True)
  nitrogen_factor = Column(Numeric(4, 2), nullable=True)
  protein_factor = Column(Numeric(4, 2), nullable=True)
  fat_factor = Column(Numeric(4, 2), nullable=True)
  carb_factor = Column(Numeric(4, 2), nullable=True)

class Langual(Base):
  __tablename__ = 'langual'

  id = Column(Integer, primary_key=True)
  ndb_number = Column(String(5), ForeignKey(FoodDescription.ndb_number),
    nullable=False)
  factor_code = Column(String(5), nullable=False)
  __table_args__ = (
    Index('idx_ndb_number_factor_code', 'ndb_number', 'factor_code',
      unique=True),
  )

class LangualFactor(Base):
  __tablename__ = 'langual_factors'

  id = Column(Integer, primary_key=True)
  factor_code = Column(String(5), ForeignKey(Langual.ndb_number),
    index=True, unique=True, nullable=False)
  description = Column(String(140), nullable=False)

class SourceCode(Base):
  __tablename__ = 'source_codes'

  id = Column(Integer, primary_key=True)
  code = Column(String(2), index=True, unique=True, nullable=False)
  description = Column(String(60), nullable=False)

class DerivationCode(Base):
  __tablename__ = 'derivation_codes'

  id = Column(Integer, primary_key=True)
  code = Column(String(4), index=True, unique=True, nullable=False)
  description = Column(String(120), nullable=False)

class NutrientData(Base):
  __tablename__ = 'nutrient_data'

  id = Column(Integer, primary_key=True)
  ndb_number = Column(String(5), ForeignKey(FoodDescription.ndb_number),
    nullable=False)
  nutrient_number = Column(String(3),
    ForeignKey(NutrientDefinition.nutrient_number), nullable=False)
  nutrient_value = Column(Numeric(10, 3), nullable=False)
  num_data_points = Column(Integer, nullable=False)
  standard_error = Column(Numeric(8, 3), nullable=True)
  source_code = Column(String(2), ForeignKey(SourceCode.code), nullable=False)
  derivation_code = Column(String(4), ForeignKey(DerivationCode.code),
    nullable=True)
  reference_ndb_number = Column(String(5),
    ForeignKey(FoodDescription.ndb_number), nullable=True)
  fortified = Column(String(1), nullable=True)
  num_studies = Column(SmallInteger, nullable=True)
  min_value = Column(Numeric(10, 3), nullable=True)
  max_value = Column(Numeric(10, 3), nullable=True)
  degrees_of_freedom = Column(SmallInteger, nullable=True)
  low_error_bound = Column(Numeric(10, 3), nullable=True)
  upper_error_bound = Column(Numeric(10, 3), nullable=True)
  stat_comments = Column(String(10), nullable=True)
  last_modified = Column(String(10), nullable=True)
  confidence_code = Column(String(1), nullable=True)
  __table_args__ = (
    Index('idx_ndb_number_nutrient_number', 'ndb_number', 'nutrient_number',
      unique=True),
  )

class Weight(Base):
  __tablename__ = 'weights'

  id = Column(Integer, primary_key=True)
  ndb_number = Column(String(5), ForeignKey(FoodDescription.ndb_number),
    nullable=False)
  sequence_number = Column(String(2), nullable=False)
  amount = Column(Numeric(5, 3), nullable=False)
  measure_description = Column(String(84), nullable=False)
  gram_weight = Column(Numeric(7, 1), nullable=False)
  num_data_points = Column(SmallInteger, nullable=True)
  standard_deviation = Column(Numeric(7, 3), nullable=True)
  __table_args__ = (
    Index('idx_ndb_number_sequence_number', 'ndb_number', 'sequence_number',
      unique=True),
  )

class Footnote(Base):
  __tablename__ = 'footnotes'

  id = Column(Integer, primary_key=True)
  ndb_number = Column(String(5), ForeignKey(FoodDescription.ndb_number),
    nullable=False)
  footnote_number = Column(String(4), nullable=False)
  footnote_type = Column(String(1), nullable=False)
  nutrient_number = Column(String(3),
    ForeignKey(NutrientDefinition.nutrient_number), nullable=True)
  footnote_text = Column(String(200), nullable=False)

class DataSource(Base):
  __tablename__ = 'data_sources'

  id = Column(Integer, primary_key=True)
  data_source_id = Column(String(6), index=True, unique=True,
    nullable=False) # given ID
  authors = Column(String(255), nullable=True)
  title = Column(String(255), nullable=False)
  year = Column(String(4), nullable=True)
  journal = Column(String(135), nullable=True)
  volume_city = Column(String(16), nullable=True)
  issue_state = Column(String(5), nullable=True)
  start_page = Column(String(5), nullable=True)
  end_page = Column(String(5), nullable=True)

class DataSourceLink(Base):
  __tablename__ = 'data_sources_link'

  id = Column(Integer, primary_key=True)
  ndb_number = Column(String(5), ForeignKey(FoodDescription.ndb_number),
    nullable=False)
  nutrient_number = Column(String(3),
    ForeignKey(NutrientDefinition.nutrient_number), nullable=False)
  data_source_id = Column(String(6), ForeignKey(DataSource.data_source_id),
    nullable=False)
  __table_args__ = (
    Index('idx_ndb_number_nutrient_number_data_source_id', 'ndb_number',
      'nutrient_number', 'data_source_id', unique=True),
  )
