import datetime
import unittest
import logging


class LoggingTestSuite(unittest.TestCase):
    """Logging test cases."""

    def test_logging(self):

        # create logger
        logger = logging.getLogger(__name__)
        # Set level
        logger.setLevel(logging.DEBUG)

        # create console file handler and set level to debug
        log_filename = "debug_" + datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
        fh = logging.FileHandler(filename=log_filename)
        fh.setLevel(logging.DEBUG)
        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - \n\t%(message)s')
        # add formatter to fh
        fh.setFormatter(formatter)
        # add fh to logger
        logger.addHandler(fh)

        # 'application' code
        logger.debug('debug message')
        logger.info('info message')
        logger.warn('warn message')
        logger.error('error message')
        logger.critical('critical message')

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()