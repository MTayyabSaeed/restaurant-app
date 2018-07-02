#file: create_session.py
#
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from database_setup import Base, MenuItem, Restaurant

engine = create_engine('sqlite:///restaurantmenu.db')        # connecting to the database we use create_engine(). In this case its sqlite db
Base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()

# quering the first restaurant from Restaurant class
first_restaurant = session.query(Restaurant).first()
# quering the first menu item from MenuItem class
first_menu_item = session.query(MenuItem).first()
#quering total restaurants from Restaurant class
total_restaurants = session.query(Restaurant).all()
#quering total restaurants from MenuItem class
total_menu_items = session.query(MenuItem).all()


def delete_all_restaurants():
    iterator = 0
    for single_entry in total_restaurants:
        iterator += 1
        session.query(Restaurant).filter(Restaurant.id == iterator).delete()
        session.commit()
    if first_restaurant:
        print("Restaurant Table is not empty")
    else:
        print("Deleted all restaurants")

def delete_all_menuitems():
    iterator = 0
    for menu_item in total_menu_items:
        iterator += 1
        session.query(MenuItem).filter(MenuItem.id == iterator).delete()
        session.commit()
    print("Deleted all menu items")

# import contextlib
# from sqlalchemy import MetaData
# 
# meta = MetaData()
# 
# with contextlib.closing(engine.connect()) as con:
#     trans = con.begin()
#     for table in reversed(meta.sorted_tables):
#         con.execute(table.delete())
#         trans.commit()

def show_all_restaurants():
	for restaurant in total_restaurants:
		print(restaurant)

def show_all_menuitems():
	for menuitem in total_menu_items:
		print(menuitem)
 
show_all_restaurants()
print("\n")
show_all_menuitems()
#print(first_menu_item.id)
print(first_restaurant)
#print(first_restaurant.name)



