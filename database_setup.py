''' Don't mind comments they are for a reason that serves me.'''

import os
import sys                                                           # provides a number of functions and variables that can manipulate different parts of python runtime environment
from sqlalchemy import Column, ForeignKey, Integer, String           # import the given classes from sqlalchemy. They will used in writing mapper code
from sqlalchemy.ext.declarative import declarative_base              # used in the configuration and class code
from sqlalchemy.orm import relationship                              # will help in making key relationships. This tool will be used when we write our mapper
from sqlalchemy import create_engine                                 # will be used at the configuration code at the end of the class
Base = declarative_base()                                            # declarative base will let sqlalchemy know that our classes are special sqlalchemy classes that ccorresponds to tables in our database


class Restaurant(Base):                                              # Restaurant base class
        
    __tablename__ = 'restaurant'                                     # resturant is the table name

    name = Column(String(80), nullable = False)                      # has name of String size 80 characters and entry cannot be created if name of restaurant is not entered
    id = Column(Integer, primary_key = True)                         # restaurant table has another column having id as the primary key for each row

    def __repr__(self):
        return "<Restaurant('{},{}')>".format(self.id, self.name)

class MenuItem(Base):                                                # MenuItem class
    __tablename__ = 'menu_item'                                      # table name is menu_item
    
    name = Column(String(250), nullable = False)                     # has a name of upto 250 character and entry cannot created if name of the menuitem is not entered 
    id = Column(Integer, primary_key = True)                         # each row would have an id which would act as primary key                         
    course = Column(String(250))                                     # course column has string size upto 250 characters
    description = Column(String(250))                                # description of each menuitem as a column and having as string size upto 250 characters 
    price = Column(String(8))                                        # price is another column of menuitem having a string size of 8 characters
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))     # restaurant_id is the foriegn key connecting 2 tables meaning, pick the restaurant id number of the restaurant when I ask for 'restaurant_id' which would mean to assign a specific menuitem to a particular restaurant
    restaurant = relationship(Restaurant)                            # creating a variable 'restaurant' to make a relationship with the class Restaurant

    def __repr__(self):
        return "<MenuItem('{},{},{},{},{},{}')>".format(self.id, self.name, self.course, self.description, self.price, self.restaurant_id)

######insert at end of file #######
engine = create_engine('sqlite:///restaurantmenu.db')                # we are using sqlite 3 and the create_engine() will create a new file that we can use similarly to a more robustdatabase like SQL or POSTGRES

Base.metadata.create_all(engine)                                     # This creates our schema as MetaData has limited schema generation commands to the database
