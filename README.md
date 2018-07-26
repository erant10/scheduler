## Scheduler with Logging

Based on [schedule](https://github.com/dbader/schedule) - An in-process scheduler integrated with logging for periodic jobs that uses the builder pattern for configuration. Schedule lets you run Python functions (or any other callable) periodically at pre-determined intervals using a simple, human-friendly syntax.

Docs: https://schedule.readthedocs.io/en/stable.


The scheduler.SafeSchedule module adds a logger and exception handling capabilities to the [schedule](https://github.com/dbader/schedule) module.

-------------------------------------------------------------------------------------------------------------------------------------------------

### Usage
All dependencies are listed in the `requirements.txt` file. Install using pip:

```{shell}
pip install requirements.txt
```

Execute from `main.py` :

```{python}
    scheduler = SafeScheduler()
    job = job(logger=scheduler.logger)
    # Set the schedule time
    scheduler.every().day.at("23:59").do(job.do_something).tag('job_tag')
    scheduler.logger.info("Starting scheduler")
    while True:
        scheduler.run_pending()
        # wake every hour
        time.sleep(60 * 60)
```

After editing `main.py`, run in the background (on linux):

```{shell}
nohup python main.py &
```


Once an instance of SafeScheduler is created, its internal logger can be passed along to the desired task.

### Structure
* ***scheduler***: The package containing the SafeSchedule implementation.
* ***job***: An example package containing a simple function (send_data_to_melingo) which exports a JSON object containing a Watson
Assistant workspace and forwards via POST the JSON to melingo api.
* ***tests***: Some test cases.
* ***main.py***: The execution file.