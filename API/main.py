from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import urllib.parse

app = Flask(__name__)

# MSSQL Database Config
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=LAPTOP-CBR1UDTQ;"
    "DATABASE=Meetings;"
    "UID=sa;"
    "PWD=GURkan5391."
)
# Set URI for SQLAlchemy configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
# Turn off SQLALCHEMY_TRACK_MODIFICATIONS setting necessary for tracking changes
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Marshmallow objects
db = SQLAlchemy(app)
ma = Marshmallow(app)


# Meeting class/model, represented as a table in the database by SQLAlchemy
class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String)
    startDate = db.Column(db.String)
    startTime = db.Column(db.String)
    endTime = db.Column(db.String)
    participants = db.Column(db.String(200))

    def __init__(self, subject, startDate, startTime, endTime, participants):
        self.subject = subject
        self.startDate = startDate
        self.startTime = startTime
        self.endTime = endTime
        self.participants = participants



# Meeting schema used for serializing data into JSON format
class MeetingSchema(ma.Schema):
    class Meta:
        fields = ('id', 'subject', 'startDate', 'startTime', 'endTime', 'participants')


# Initialize schema objects
meeting_schema = MeetingSchema()
meetings_schema = MeetingSchema(many=True)

# Create Meeting
@app.route('/meeting', methods=['POST'])
def add_meeting():
    # Get the incoming JSON data
    data = request.json
    if not data:
        return jsonify({'message': 'No data provided'}), 400

    # Get the required fields
    subject = data.get('subject')
    startDate = data.get('startDate')
    startTime = data.get('startTime')
    endTime = data.get('endTime')
    participants = data.get('participants')

    # Check for missing fields
    if not all([subject, startDate, startTime, endTime, participants]):
        return jsonify({'message': 'Missing required fields'}), 400

    # Create a new meeting object and add it to the database
    new_meeting = Meeting(subject, startDate, startTime, endTime, participants)
    db.session.add(new_meeting)
    db.session.commit()

    return meeting_schema.jsonify(new_meeting), 201

# Get All Meeting
@app.route('/meeting', methods=['GET'])
def get_meetings():
    all_meetings = Meeting.query.all()
    result = meetings_schema.dump(all_meetings)
    return jsonify(result)


# Get Single Meeting
@app.route('/meeting/<id>', methods=['GET'])
def get_meeting(id):
    meeting = Meeting.query.get(id)
    return meeting_schema.jsonify(meeting)


# Update Meeting
@app.route('/meeting/<id>', methods=['PUT'])
def update_meeting(id):
    meeting = Meeting.query.get(id)

    # Get new data
    subject = request.json['subject']
    startDate = request.json['startDate']
    startTime = request.json['startTime']
    endTime = request.json['endTime']
    participants = request.json['participants']

    # Update meeting data and commit to the database
    meeting.subject = subject
    meeting.startDate = startDate
    meeting.startTime = startTime
    meeting.endTime = endTime
    meeting.participants = participants

    db.session.commit()

    return meeting_schema.jsonify(meeting)


# Delete Meeting
@app.route('/meeting/<id>', methods=['DELETE'])
def delete_meeting(id):
    meeting = Meeting.query.get(id)
    db.session.delete(meeting)
    db.session.commit()
    return meeting_schema.jsonify(meeting)


if __name__ == '__main__':
    app.run(debug=True)
