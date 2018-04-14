from app import stores
from app import dummy_data
from flask import Flask
app = Flask(__name__)


member_store = stores.MemberStore()
post_store = stores.PostsStore()
dummy_data.seed_stores(member_store, post_store)
#from views import* for local
from app import views
from app import api.py
