import os

from fastapi import FastAPI
import uvicorn
from utils import utils
import logging

app = FastAPI()

# Create a logger with handler
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

# Create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@app.get("/")
def read_root():
    return "Welcome to the fibonacci app. Use end point /is-fibonacci?number=1 to start"

@app.get("/is-fibonacci")
def is_fibonacci(number: int):
    logger.debug(f"received request for number {number}")
    try:
        if utils.is_fibonacci_number(number):
            return f"next fibonacci is: {utils.fibonnacci(number)}"
        else:
            return "not a Fibonacci number"
    except Exception as e:
        logger.error(f"An error occurred: {e}")

        return "there was an internal error processing the number"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("WEB_PORT","8000")))
