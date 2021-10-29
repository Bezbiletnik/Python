import logging


def add(x, y):
    logging.info('added {} and {} to get {}'.format(x, y, x+y))
    return x+y