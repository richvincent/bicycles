from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey,\
    Date
"""Bike industry Management System Module

Please use the classes and functions contained in this module to design your
Bicycle Industry Management needs.

"""


engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbicycles')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Bike_Shop(Base):
    __tablename__ = "Bike_Shop"

    store_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Bicycle(Base):
    __tablename__ = "Bicycle"

    model_name = Column(String, primary_key=True)
    model_description = Column(String, nullable=False)
    cost_to_produce = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)


class Customers(Base):
    __tablename__ = "customers"

    customer_number = Column(Float, primary_key=True)
    customer_name = Column(String, nullable=False)
    budget = Column(Float, nullable=False)


class Inventoy(Base):
    __tablename__ = "inventory"
    inv_id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey('Bike_Shop.store_id'), nullable=False)
    model_name = Column(String, ForeignKey('Bicycle.model_name'),
                        nullable=False)
    last_update = Column(DateTime, default=datetime.utcnow)


class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True)
    customer_number = Column(Integer, ForeignKey('customers.customer_number'),
                             nullable=False)
    model_name = Column(String, ForeignKey('Bicycle.model_name'),
                        nullable=False)
    date_time = Column(DateTime, default=datetime.utcnow)
    price = Column(Float, nullable=False)
    store_id = Column(Integer, ForeignKey('Bike_Shop.store_id'), nullable=False)


Base.metadata.create_all(engine)




