import logging
logging.basicConfig(filename = 'summary.log',level=logging.INFO)
def check_age(age):
    if age<18:
        logging.warning("keep away from children")
    else:
        logging.info("you are eligible")

check_age(22)        


