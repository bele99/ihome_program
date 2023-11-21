# coding:utf-8

from . import db
from datetime import datetime
#from ihome import constants

class BaseModel(object):
    """ Base Model: adding Create Time and Update Time for each model."""
    create_time = db.Column(db.DateTime, default=datetime.now) # Recording the Create Time
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) # Recoding the Update Time

class User(BaseModel, db.Model):
    """ User """

    __tablename__ = "ih_user_profile"

    id = db.Column(db.Integer, primary_key=True) # user id
    name = db.Column(db.String(32), unique=True, nullable=False) # user name
    password_hash = db.Column(db.String(128), nullable=False)  # Encrypted password
    mobile = db.Column(db.String(11), unique=True, nullable=False)  # phone number
    real_name = db.Column(db.String(32))  # real name
    id_card = db.Column(db.String(20))  # ID card
    avatar_url = db.Column(db.String(128))  # Avatar url
    houses = db.relationship("House", backref="user")  # user published housing information
    orders = db.relationship("Order", backref="user")  # Orders placed by users

class Area(BaseModel, db.Model):
    """ Area """

    __tablename__ = "ih_area_info"

    id = db.Column(db.Integer, primary_key=True)  # area id
    name = db.Column(db.String(32), nullable=False)  # area name
    houses = db.relationship("House", backref="area")  # Houses in the area

# House Facility table, Establishing a many-to-many relationship between houses and facilities.
house_facility = db.Table(
    "ih_house_facility",
    db.Column("house_id", db.Integer, db.ForeignKey("ih_house_info.id"), primary_key=True),  # House ID
    db.Column("facility_id", db.Integer, db.ForeignKey("ih_facility_info.id"), primary_key=True)  # Facility ID
)

class House(BaseModel, db.Model):
    """ House Information"""

    __tablename__ = "ih_house_info"

    id = db.Column(db.Integer, primary_key=True)  # House ID
    user_id = db.Column(db.Integer, db.ForeignKey("ih_user_profile.id"), nullable=False)  # User ID of the house owner
    area_id = db.Column(db.Integer, db.ForeignKey("ih_area_info.id"), nullable=False)  # Area number of the house location
    title = db.Column(db.String(64), nullable=False)  # Title on the posts
    price = db.Column(db.Integer, default=0)  # Price
    address = db.Column(db.String(512), default="")  # Address
    room_count = db.Column(db.Integer, default=1)  # Room number
    acreage = db.Column(db.Integer, default=0)  # Housing area
    unit = db.Column(db.String(32), default="")  # Housing units
    capacity = db.Column(db.Integer, default=1)  # Number of people accommodated in the house
    beds = db.Column(db.String(64), default="")  # Number of Beds in the House
    deposit = db.Column(db.Integer, default=0)  # Housing deposit
    min_days = db.Column(db.Integer, default=1)  # Minimum check-in days
    max_days = db.Column(db.Integer, default=0)  # Maximum check-in days, 0 indicates no limit
    order_count = db.Column(db.Integer, default=0)  # Number of completed orders for this property
    index_image_url = db.Column(db.String(256), default="")  # The url path of the house owner's image
    facilities = db.relationship("Facility", secondary=house_facility)  # House facility
    images = db.relationship("HouseImage")  # house image
    orders = db.relationship("Order", backref="house")  # house order

class Facility(BaseModel, db.Model):
    """ Facility Information """
    
    __tablename__ = "ih_facility_info"

    id = db.Column(db.Integer, primary_key=True)  # Facility ID
    name = db.Column(db.String(32), nullable=False)  # Facility Name

class HouseImage(BaseModel, db.Model):
    """ House Image"""

    __tablename__ = "ih_house_image"

    id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer, db.ForeignKey("ih_house_info.id"), nullable=False)  # 房屋编号
    url = db.Column(db.String(256), nullable=False)  # The url path of image

class Order(BaseModel, db.Model):
    """ Order """

    __tablename__ = "ih_order_info"

    id = db.Column(db.Integer, primary_key=True)  # Order ID
    user_id = db.Column(db.Integer, db.ForeignKey("ih_user_profile.id"), nullable=False)  # User ID for placing the order
    house_id = db.Column(db.Integer, db.ForeignKey("ih_house_info.id"), nullable=False)  # Room number reserved
    begin_date = db.Column(db.DateTime, nullable=False)  # Starting time of reservation
    end_date = db.Column(db.DateTime, nullable=False)  # End time of reservation
    days = db.Column(db.Integer, nullable=False)  # Total number of days booked
    house_price = db.Column(db.Integer, nullable=False)  # Unit price of the house
    amount = db.Column(db.Integer, nullable=False)  # The total amount of the order
    status = db.Column(  # Status of the order
        db.Enum(
            "WAIT_ACCEPT",
            "WAIT_PAYMENT",
            "PAID",
            "WAIT_COMMENT",
            "COMPLETE",
            "CANCELED",
            "REJECTED"  # Rejected
        ),
        default="WAIT_ACCEPT", index=True)
    comment = db.Column(db.Text)  # Comment information or reason for rejection of the order
