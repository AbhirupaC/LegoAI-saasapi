from ..logger import log

class Pool:
	r = None
	max_retries = 3 
	@classmethod
	def __attemptConnection__(cls):
		import redis
		from conf import APP_CONFIG
		try:
			if cls.r == None:
				print("initializing redis connection")
				pool = redis.ConnectionPool(
					host=APP_CONFIG["REDIS_HOST"], 
					port=APP_CONFIG["REDIS_PORT"], 
					db=0
				)
				cls.r = redis.Redis(
					connection_pool = pool, 
					max_connections = APP_CONFIG["REDIS_MAX_CONNECTIONS"]
				)
				print("redis connection established")
		except Exception as e:
			cls.r = None
			print("Failed to establish connection to redis")
		

	@classmethod
	def getConnection(cls):
		counter = 0
		while counter <  cls.max_retries:
			cls.__attemptConnection__()
			try:
				if cls.r.ping():
					break
			except Exception as e:
				log.error(e)
				print("retrying to connect to redis: ", counter)
				counter = counter + 1
			continue
		return cls.r
	
	@classmethod
	def releaseConnection(cls, conn):
		conn.release()
