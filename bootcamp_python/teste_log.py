import logging

logging.basicConfig(
    filename='infoLog.log',
    level=logging.DEBUG,
    format='%(levelname)s %(asctime)s: %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)

# Para que o log apareca no terminal
# logger = logging.StreamHandler()
# logging.getLogger('').addHandler(logger)

logging.debug('Insto é uma mensagem nível debug')
logging.info('Insto é uma mensagem nível info')
logging.warning('Insto é uma mensagem nível warningg')
logging.error('Insto é uma mensagem nível error')
logging.critical('Insto é uma mensagem nível critial')