class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///database.db"
    SECRET_KEY = "this is a secret"
    UPLOADS_AUTOSERVE = True