from flask import Flask, render_template, request, redirect, url_for, flash

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()

app = Flask(__name__)


@app.route('/restaurants/')
def restaurants():
    restaurants = session.query(Restaurant).all()
    if restaurants:
        return render_template('restaurants.html', restaurants=restaurants)
    else:
        return "Request couldn't Found"


@app.route('/restaurants/<int:restaurant_id>/')
def restaurant_menu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    menu_items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    if menu_items:
        return render_template('restaurantmenu.html',
                               restaurant=restaurant, menu_items=menu_items)
    else:
        return "No Menus Found"


@app.route('/restaurants/<int:restaurant_id>/create-menu-item/',
           methods=['GET', 'POST'])
def create_menu_item(restaurant_id):
    if request.method == 'POST':
        new_menu_item = MenuItem(name=request.form['new_menu_item'],
                                 course=request.form['item_course'],
                                 description=request.form['item_desc'],
                                 price=request.form['item_price'],
                                 restaurant_id=restaurant_id)
        
        session.add(new_menu_item)
        session.commit()
        flash("New menu item: '" + str(new_menu_item.name) + "' has been created!")
        return redirect(url_for('restaurant_menu', restaurant_id=restaurant_id))
    else:
        return render_template('createnewmenu.html', restaurant_id=restaurant_id)


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit-menu-item/', 
           methods=['GET', 'POST'])
def edit_menu_item(restaurant_id, menu_id):
    menu_item_to_edit = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        menu_item_to_edit.name = request.form['item_name']
        menu_item_to_edit.course = request.form['item_course']
        menu_item_to_edit.description = request.form['item_desc']
        menu_item_to_edit.price = request.form['item_price']

        session.add(menu_item_to_edit)
        session.commit()
        flash("Menu item: '" + str(menu_item_to_edit.name) + "' has been edited!")
        return redirect(url_for('restaurant_menu', restaurant_id=restaurant_id))
    else:
        return render_template('editmenuitem.html', restaurant_id=restaurant_id,
                               menu_item=menu_item_to_edit)


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete-menu-item/', 
           methods=['GET', 'POST'])
def delete_menu_item(restaurant_id, menu_id):
    item_to_delete = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(item_to_delete)
        session.commit()
        flash("Menu item '" + str(item_to_delete.name)+ "' has been successfully deleted." )
        return redirect(url_for('restaurant_menu', restaurant_id=restaurant_id))
    else:
        return render_template('deletemenuitem.html', restaurant_id=restaurant_id, 
                               menu_item=item_to_delete)



if __name__ == '__main__':
    app.secret_key = 'super-secret-key'
    app.debug = True
    app.run(host='127.0.0.1', port=5001)



