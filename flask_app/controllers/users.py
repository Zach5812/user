from flask_app import app, render_template, redirect, request
from flask_app.models.user import User


# Create

@app.route("/new")
def new():
    return render_template("new.html")


@app.route("/create", methods=['post'])
def create_user():
    User.save(request.form)
    return redirect("/")


# Read All
@app.route("/")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("read.html", users=users)

# NEW USER


@app.route("/user/<int:id>")
def show(id):
    data = {'id': id}
    user = User.get_user(data)
    return render_template("show.html", user=user)

# EDIT


@app.route("/user/<int:id>/edit")
def edit(id):
    data = {'id': id}
    user = User.get_user(data)
    return render_template("edit.html", user=user)


@app.route("/edit", methods=['post'])
def edit_user():
    print(request.form)
    User.update(request.form)
    return redirect("/")


# DELETE
@app.route("/user/<int:id>/delete")
def destroy(id):
    User.delete(id)
    return redirect("/")