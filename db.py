# -*- coding: utf-8 -*-

import config
import pymongo

# Método para acceder a una colección en una BD, si no existe se crea
def getCollection(dbName,colName):
	# Connection to Mongo DB
	try:
	    conn=pymongo.MongoClient()
	    print "Connected successfully!!!"
	except pymongo.errors.ConnectionFailure, e:
	   print "Could not connect to MongoDB: %s" % e 
	
	# Busca una base de datos y si no, la crea
	db=conn[dbName]

	# Busca una colección y si no, la crea
	col = db[colName]

	return col

