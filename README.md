Basic CRUD app
=============


This repo contains an example of my work on a simple CRUD app.


The following links give an overview of the app and its workings.

* [ The Model ]("https://github.com/ceejaay/ox_crud_app/blob/main/todo_items/models.py")
    This is a simple model. It only has one property. This model is in _another_ app in this Django project. One
    features of Django is you can use models from one app in another without duplicating code.

* [ The Seralizer ]("https://github.com/ceejaay/ox_crud_app/blob/main/todo_api/serializers.py")
    In Django/Python. A serializeris requred to translate JSON objects from and to Python objects.
    The Serializer gets data from the Item model.

* [The View]("https://github.com/ceejaay/ox_crud_app/blob/main/todo_api/views.py")
    Much of the app's heavy lifting is in the view. There are two functions in this view class.
    1. items
    2. single_item


    The `item` function checks for two values in the request `POST` and `GET`. If it is `POST` this endpoint will create
    a new Todo item. A `GET` request retrieves a list of all the Todo items.
    The `single_item` function handles the remainder of the HTTP verbs. The function relys on getting an ID from the
    http request.
    It includes `GET` to get one Todo item.
    `DELETE` which retrieves the resource from the database and then deletes it.
    `PUT` This allows the resource to update. Like `GET` and `DELETE` it requires the resource from the database.
    The functions return the appropriate status codes when used.

* [The Routes]("https://github.com/ceejaay/ox_crud_app/blob/main/todo/urls.py")
    The routes starting on line 22 designate where the endpoints can be accessed.
    Routes require the viewset functions and they need permission to use the correct http verb.

