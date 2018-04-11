from flask import Flask,render_template,request,redirect,url_for
from app import models,stores
from app import app,member_store,post_store
from app import stores
edit_post_id=0
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

@app.route("/topic/show/<id>")
def topic_show(id):
    post=post_store.get_by_id(int(id))
    return post.content


@app.route("/topic/edit/<id>",methods = ["GET", "POST"])
def topic_edit(id):
    edit_post_id=int(id)
    if request.method=="POST":
        post=post_store.get_by_id(edit_post_id)
        new_content=request.form["new content"]
        post.content=new_content
        return redirect(url_for("home"))
    else:
        return render_template("topic_edit.html")
