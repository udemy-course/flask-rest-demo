
class Config:
    # SQLALCHEMY_DATABASE_URI = "sqlite:///demo.db"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/demo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
