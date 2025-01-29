from flask import Blueprint
from flask_restful import Resource, Api
from .response import custom_response
from .schema import response
from datetime import datetime, timezone
import logging

api_blueprint = Blueprint("api", __name__, url_prefix="/api/hng") 
api = Api(api_blueprint)

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create handlers
file_handler = logging.FileHandler('logs/api.log')
console_handler = logging.StreamHandler()

# Create formatters and add it to handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def get_current_date():
    now = datetime.now(timezone.utc)
    iso_format = now.isoformat() + "Z"
    return iso_format

class Task(Resource):
    def __init__(self):
        self.response = custom_response

    def get(self):
        try:
            time = get_current_date()
            data = {
                "email": "nkangprecious26@gmail.com", 
                "current_datetime": time,
                "github_url": "https://github.com/Prevz26/HNG-TASK-0.git"
            }
            logger.info(data)
            final_data = response.dump(data)
            logger.info(final_data)
            return final_data
        except Exception as e:
            logger.error(f"Error in Task.get(): {str(e)}") 
            return self.response.error_response(message=str(e), status_code=500)  

api.add_resource(Task, "/backend/task0")