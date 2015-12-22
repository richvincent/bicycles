from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
"""Bike industry Management System Module

Please use the classes and functions contained in this module to design your
Bicycle Industry Management needs.

"""


engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbicycles')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Shop(Base):
    __tablename__ = "shops"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    margin = Column(Float, nullable=False)


class Bike(Base):
    __tablename__ = "bikes"

    id = Column(String, primary_key=True)
    description = Column(String, nullable=False)
    cost = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    budget = Column(Float, nullable=False)


class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey('bikes.id'), nullable=False)
    store = relationship("Shop", backref="inventory")
    model_name = Column(String, ForeignKey('bikes.id'),
                        nullable=False)
    model = relationship("Bike", backref="inventory")
    last_update = Column(DateTime, default=datetime.utcnow)


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    customer_number = Column(Integer, ForeignKey('customers.id'),
                             nullable=False)
    customer = relationship("Customer", backref="transactions")
    model_name = Column(String, ForeignKey('bikes.id'),
                        nullable=False)
    model = relationship("Bike", backref="transactions")
    date_time = Column(DateTime, default=datetime.utcnow)
    price = Column(Float, nullable=False)
    store_id = Column(Integer, ForeignKey('shops.id'), nullable=False)
    store = relationship("Shop", backref="transactions")


Base.metadata.create_all(engine)
