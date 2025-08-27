#Using logger in real eaxmple by making a calculator app 
import logging

#Logging Setting
logging.basicConfig(
    level=logging.DEBUG,
    format= ' %(asctime)s - %(name)s - %(levelname)s - %(message)s ',
    datefmt= '%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('ArithematicApp')

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def subtract(a,b):
    result = a-b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result
    
def multiply(a,b):
    result = a*b
    logger.debug(f"Multiplyig {a} * {b} = {result}")
    return result

def division(a,b):
    try:
        result = a/b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None

add(10,20)
subtract(40,20)
multiply(10,30)
division(40,25) 
