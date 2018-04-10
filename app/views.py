from flask import Flask,render_template,request,redirect,url_for
from app import models,stores
from app import app,member_store,post_store
from app import stores
@app.route("/")
@app.route("/index")
def home():
  return render_template("index.html", posts = post_store.get_all())

@app.route("/topic/add" ,methods = ["GET", "POST"])
def topic_add():
    if request.method=="POST":
        new_post = models.Post(request.form["title"], request.form["content"])
        post_store.add(new_post)
        return redirect(url_for("home"))
    else:
        return render_template("topic_add.html")

@app.route("/topic/delete/<id>")
def topic_delete(id):
  post_store.delete(int(id))
  return redirect(url_for("home"))
