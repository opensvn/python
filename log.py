#!/usr/bin/evn python
#-*- coidng: utf-8 -*-

import logging

logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occured')
logging.critical('Critical error -- shutting down')
