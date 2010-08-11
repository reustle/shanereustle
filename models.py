from pymongo import Connection
from gridfs import GridFS
from pymongo.objectid import ObjectId
from pymongo.errors import OperationFailure, AutoReconnect
from datetime import datetime, timedelta
import settings

class DatabaseClass():
	mongohq = 0
	def connect(self):
		self.mongohq = Connection( settings.DB_SERVER , settings.DB_PORT )
		self.authenticate()
	
	def authenticate(self):		
		self.mongohq.shanereustle.authenticate( settings.DB_USER , settings.DB_PASS )
		self.mongohq.shanereustle.log.insert({ "type":"notice" , "message":"Authenticating MongoHQ Connection","timestamp": ( datetime.today() - timedelta(hours=4)  )   })
	
	def keep_alive(self):
		self.authenticate()
		
db = DatabaseClass()
db.connect()

class AccountsClass():
	def try_login(self, login_email , login_password ):
		return False
		
	def verify_session(self):
		return False

class BlogClass():
	def get_entries(self):
		db.keep_alive()
		
		#return list( mongohq.shanereustle.blog.find().sort({"date":1}).skip(skip).limit(limit) )
		return list( db.mongohq.shanereustle.blog.find().limit(6) )
	
	def get_entry(self, entry_query):
		db.keep_alive()
		
		return db.mongohq.shanereustle.blog.find_one({"url_hash":entry_query})
	
	def search_entries(self, search_query):
		db.keep_alive()
		
		return list( db.mongohq.shanereustle.blog.find({"keywords":search_query}) )
	
	def list_keywords(self):
		db.keep_alive()
		
		entries = list( db.mongohq.shanereustle.blog.find() )
		keywords = {}
		for entry in entries:
			for keyword in entry["keywords"]:
				if keyword in keywords:
					keywords[keyword] += 1
				else:
					keywords.update({keyword:1})
		return list(sorted( keywords , key=keywords.__getitem__, reverse=True))
