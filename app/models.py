from .extensions import (
    db,
    login_manager,
    users_imgs,
    bcrypt,
)
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from flask_login import UserMixin
from flask import url_for
from sqlalchemy import or_
from datetime import datetime
from datetime import date
from enum import Enum
from typing import List


class UserRole(Enum):
    ADMIN = 0


class RowStatus(Enum):
    INACTIVE = 0
    ACTIVE = 1


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    image_filename = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Enum(RowStatus), nullable=False, default=RowStatus.ACTIVE)
    role = db.Column(db.Enum(UserRole), nullable=False)

    @hybrid_property
    def image_url(self):
        url = (
            url_for(
                "_uploads.uploaded_file",
                setname=users_imgs.name,
                filename=self.image_filename,
                _external=True,
            )
            if self.image_filename != None and len(self.image_filename) > 0
            else url_for("static", filename="img/users/default.png", _extenal=True)
        )
        return url
