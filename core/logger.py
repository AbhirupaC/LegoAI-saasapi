class Logger:
	logger =None
	__LOGLEVEL_MAP__ = {
		"CRITICAL" : 50,
		"ERROR" : 40,
		"WARNING" : 30,
		"INFO" : 20,
		"DEBUG" : 10,
		"NOTSET": 0
	}

	@classmethod
	def getLogger(cls):
		if cls.logger == None:
			import logging
			from core.conf import APP_CONFIG
			# setting logging
			logging.basicConfig(
				filename =APP_CONFIG.get("LOG_LEVEL", "apiservice.log"),
				level = cls.__LOGLEVEL_MAP__[ APP_CONFIG["LOG_LEVEL"].upper() ]
			)
			cls.logger =  logging
		return cls.logger
log = Logger.getLogger()