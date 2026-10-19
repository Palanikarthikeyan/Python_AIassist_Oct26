import logging

logging.basicConfig(filename="demo.log",level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt="%Y - %m -%d %H:%M:%S")

logging.info("Application process started")
logging.warning("5 records contains missing email address")
logging.error("App is critical state")