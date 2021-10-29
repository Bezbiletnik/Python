# import logging

# logging.basicConfig(filename='sample.log', level=logging.DEBUG, filemode='w')

# logging.debug('This is a debug message')
# logging.info('Informational message')
# logging.error('An error has happend!')


# import logging

# logging.basicConfig(filename='sample_2.log', level=logging.INFO)
# log = logging.getLogger('ex')

# try:
#     raise RuntimeError
# except:
#     log.exception('Error!')


# import logging
# import otherMod


# def main():
#     '''
#         The main entry point of the application 
#     '''


#     logging.basicConfig(filename='mySnake.log', level=logging.INFO)
#     logging.info('Program started')
#     result = otherMod.add(7, 8)
#     logging.info('Done!')

# if __name__=='__main__':
#     main()


import logging
import otherMod2


def main():
    logger = logging.getLogger('exampleApp')
    logger.setLevel(logging.INFO)

    #create the logging file handler
    fh = logging.FileHandler('new_snake.log')

    formatter = logging.Formatter('%(asctime)s - %(name)s - \
                                    %(levelname)s - %(message)s')
        