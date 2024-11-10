# This code is used to create a log file and set up logging for our program.
# A log file is like a diary where our program writes down what it's doing.

import logging
import os
from datetime import datetime

# We want to name our log file with the current date and time, so it's easy to tell when it was made.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# We want to put our log file in a special folder called "logs", so it's easy to find.
logs_path = os.path.join(os.getcwd(), "logs")

# If the "logs" folder doesn't exist, we want to create it.
os.makedirs(logs_path, exist_ok=True)

# Now we can put our log file in the "logs" folder.
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# This is where we set up our logging. We want to write our logs to the log file we just made.
logging.basicConfig(
    filename=LOG_FILE_PATH,
    # This is the format of each log message. It includes the date and time, the line number, the name of the logger, the level of the log, and the message.
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    # We want to log everything at the INFO level or higher.
    level=logging.INFO,
)

# if __name__ == "__main__":
#     logging.info("Logging has started")