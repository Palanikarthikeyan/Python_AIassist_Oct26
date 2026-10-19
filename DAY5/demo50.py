import logging

logging.basicConfig(level=logging.INFO,
                    format="%(levelname)s: %(message)s")

def get_balance(balance):
    try:
        result = 10000 / balance
        logging.info("Balance Calculation is done")
        return result
    except Exception:
        logging.exception("Balance calculation failed")
        return None


print(get_balance(2))
print(get_balance(0))