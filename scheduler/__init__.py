from traceback import format_exc
import logging
from schedule import Scheduler
import datetime


class SafeScheduler(Scheduler):
    """
    An implementation of Scheduler for a specific job at fixed intervals
    If the job fails, logs their exception tracebacks as errors, optionally reschedules the jobs for their
    next run time, and keeps going.
    source: https://gist.github.com/mplewis/8483f1c24f2d6259aef6
    """
    def __init__(self, reschedule_on_failure=True):
        """
        If reschedule_on_failure is True, jobs will be rescheduled for their
        next run as if they had completed successfully. If False, they'll run
        on the next run_pending() tick.
        """
        self.reschedule_on_failure = reschedule_on_failure
        self.log_name = 'kpmg_' + datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
        self.logger = self.init_logger()
        super().__init__()

    def init_logger(self):
        logger = logging.getLogger(__name__)
        # Set level
        logger.setLevel(logging.DEBUG)
        # create console file handler and set level to debug
        log_filename = self.log_name
        fh = logging.FileHandler(filename=log_filename)
        fh.setLevel(logging.DEBUG)
        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # add formatter to fh
        fh.setFormatter(formatter)
        # add fh to logger
        logger.addHandler(fh)
        return logger

    def _run_job(self, job):
        try:
            super()._run_job(job)
        except Exception:
            self.logger.error(format_exc())
            job.last_run = datetime.datetime.now()
            job._schedule_next_run()

