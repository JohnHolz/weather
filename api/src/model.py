from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy()

class Metrics(db.Model):
    __tablename__ = "metrics"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())
    public_id = db.Column(db.String(200), unique=True)

    name = db.Column(db.String(60), nullable=False)
    model_type = db.Column(db.String(60), nullable=False)
    dataset = db.Column(db.String(60), nullable=False)
    dataset_subtype = db.Column(db.String(60), nullable=False)

    parameters = db.Column(JSON, nullable=True)
    metrics = db.Column(JSON, nullable=True)

    def json(self):
        return {
            "created_at": self.created_at,
            "model_type": self.model_type,
            "dataset": self.dataset,
            "dataset_subtype": self.dataset_subtype,
            "metrics": self.metrics
        }
    
class Station(db.Model):
    __tablename__ = "stations"
    ## "station",
    ## "region",
    ## "state",
    ## "station_code",
    ## "first date",
    ## "height",
    ## "longitude",
    ## "latitude"
    ## extra colleta


    station_code = db.Column(db.String(20),nullable=False,primary_key=True)
    station = db.Column(db.String(100),nullable=True)
    
    region = db.Column(db.String(50),nullable=True)
    state = db.Column(db.String(50),nullable=True)
    
    first = db.Column(db.DateTime,nullable=True)
    
    height = db.Column(db.Integer,nullable=True)
    longitude = db.Column(db.Integer,nullable=True)
    latitude = db.Column(db.Integer,nullable=True)

    collect = db.Column(db.Boolean, nullable=False)

