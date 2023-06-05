from fastapi import FastAPI
import uvicorn
from utils import utils
import logging

# get root logger
# logger = logging.getLogger(__name__)
# # setup loggers
# logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

app = FastAPI()


@app.get("/")
def read_root():
    return "Welcome to the fibonacci app. Use  http://0.0.0.0:8000/is-fibonacci?number=1 to start"


# TODO log to std out
# TODO Try an catch?
@app.get("/is-fibonacci")
def is_fibonacci(number: int):
    # logger.info("logging from the root logger")
    if utils.is_fibonacci_number(number):
        # Create a generator object starting from the given Fibonacci number
        return f"next fibonacci is :{utils.fibonnacci(number)}"
    else:
        return "not a Fibonacci number"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
