from sqlalchemy import Column, Integer, MetaData, String, Float, ForeignKey, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
#from sqlalchemy.orm import relationship

from settings import PostgresConfiguration
#from sqlalchemy.dialects.postgresql import UUID
#from uuid import uuid4

pg = PostgresConfiguration()
engine = create_engine(pg.postgres_db_path)
meta = MetaData(engine, schema='data_science')
Base = declarative_base(metadata=meta)


class ToidsTable(Base):
    __tablename__ = 'hrl_forest_100m'
    toid_uid = Column(String, primary_key=True)
    hrl_min = Column(Float)
    hrl_max = Column(Float)
    hrl_count = Column(Float)
    hrl_sum = Column(Float)
    hrl_mean = Column(Float)
    hrl_stdev = Column(Float)
    hrl_variance = Column(Float)
