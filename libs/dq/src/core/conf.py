from dotenv import dotenv_values

class Config():

    configs = dotenv_values(".env")

    GE_ROOT_FOLDER = configs["GE_ROOT_FOLDER"]


config = Config()
