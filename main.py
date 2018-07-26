from scheduler import SafeScheduler
import time
import job

if __name__ == '__main__':
    scheduler = SafeScheduler()
    job = job(logger=scheduler.logger)
    # Set the schedule time
    scheduler.every().day.at("23:59").do(job.do_something).tag('job_tag')
    scheduler.logger.info("Starting scheduler")
    while True:
        scheduler.run_pending()
        # wake every hour
        time.sleep(60 * 60)
