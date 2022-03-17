import coloredlogs, logging
logger=logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)
logger.info("Hola DevOps")

def add_one(number):
    return number + 1

#print(add_one(3))

# def add_one(number):
#     return number+2