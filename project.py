from flask import Flask, render_template, request, redirect, url_for, flash

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()

app = Flask(__name__)

# this route shows all the restaurants names
@app.route('/restaurants/')
def restaurants():
	restaurants = session.query(Restaurant).all()
	output = ""
	for restaurant in restaurants:
		output += restaurant.name
		output += 2*"<br>"
	return output

# this route shows the menu items from each restaurant number
@app.route('/restaurants/<int:restaurant_id>/')
def restaurant_menu(restaurant_id):
    return "Task 1 competed"

# this route will allow user to add new menu items
@app.route('/restaurants/<int:restaurant_id>/new-menu-item')
def new_menu_item(restaurant_id):
    return "Task 2 completed"

# this route will allow user to edit menu items
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit-menu-item')
def edit_menu_item(restaurant_id, menu_id):
    return "Task 3 completed"

#this route will the user to delete menu items
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete-menu-item', methods=['GET','POST'])
def delete_menu_item(restaurant_id, menu_id):
	item_to_delete = session.query(MenuItem).filter_by(id = menu_id).one()
	if request.method == 'POST':
		session.delete(item_to_delete)
		session.commit()
		return redirect(url_for('restaurant_menu', restaurant_id = restaurant_id))
	else:
		return render_template('deletemenuitem.html', restaurant_id = restaurant_id, item_to_delete = item_to_delete)

if __name__ == '__main__':
	app.secret_key = 'super-secret-key'
	app.debug = True
	app.run(host='127.0.0.1', port=5001)


