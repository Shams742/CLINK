"""
CLINK — Patient Entity
Stores patient personal and login information.
"""
from datetime import datetime
from flask_login import UserMixin
from app.extensions import db


class Patient(UserMixin, db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(255), nullable=False)  # bcrypt hash
    account_status = db.Column(db.String(20), default='active')  # active / inactive
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    role = db.Column(db.String(10), default='patient')

    # Relationships
    symptom_records = db.relationship('SymptomRecord', backref='patient', lazy='dynamic')
    appointments = db.relationship('Appointment', backref='patient', lazy='dynamic')
    notifications = db.relationship(
        'Notification',
        primaryjoin="and_(Patient.id == foreign(Notification.user_id), Notification.user_role == 'patient')",
        lazy='dynamic',
        viewonly=True
    )

    def get_id(self):
        return f"patient-{self.id}"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'accountStatus': self.account_status,
            'createdAt': self.created_at.isoformat() if self.created_at else None,
            'role': self.role
        }

    def __repr__(self):
        return f'<Patient {self.name}>'
