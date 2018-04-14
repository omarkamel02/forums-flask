@app.route("/api/topic/all")
def topic_get_all():
  posts = [post.__dict__() for post in post_store.get_all()]
  return jsonify(posts)
