# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
#
# USERNAME = "AZ_DEV_USER@adqtmstaging"
# PASSWORD = "4BuildersOn!y"
# HOST = "adqtmstaging.database.windows.net"
# DB_NAME = "athingzdev"
#
# engine = create_engine("mssql+pyodbc://{}:{}@{}/{}?driver=SQL+Server".format(USERNAME, PASSWORD, HOST, DB_NAME), pool_size=30, max_overflow=0)
# print("engine %s " % engine)
# Session = sessionmaker(bind=engine)
#
# Base = declarative_base()
#
#
