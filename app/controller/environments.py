from app import db

class Environment(db.Model):
    EnvironmentId = db.Column(db.Integer, nullable=False)
    Name = db.Column(db.Nvarchar(500), index=False)
    Description = db.Column(db.Nvarchar(None), index=False) # Nvarchar None refers to Nvarchar MAX in SQL Server DB

    def __init__(self, EnvironmentId, Name, Description)
        self.EnvironmentId = EnvironmentId
        self.Name = Name
        self.Description = Description