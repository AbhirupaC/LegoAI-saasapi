from dotenv import dotenv_values
import os
def prepare_config():
	default_config = {
		"PORT":5000,
		"LOG_LEVEL":"INFO",
		"REDIS_HOST":"localhost",
		"REDIS_PORT":6379,
		"REDIS_MAX_CONNECTIONS":2
	}
	loaded_config = dotenv_values(".env")
	os_config = {}
	os_config_prefix = "apiservice_env_"
	for _k in os.environ:
		if _k.startswith(os_config_prefix):
			os_config[_k.replace(os_config_prefix, "")] = os.environ[_k]
	return {
		**default_config, 
		**loaded_config,
		**os_config	
	}


APP_CONFIG = prepare_config()
print(APP_CONFIG)