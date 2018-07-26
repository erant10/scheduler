class Job:
    def __init__(self, logger):
        self.successful_calls = 0
        self.failed_calls = 0
        self.logger = logger

    def do_something(self):
        self.logger.info("Starting job")

        try:
            # do something

            self.logger.info("job Successful.")
            self.successful_calls += 1
        except Exception as e:
            self.logger.error("Failed sending POST to melingo. " + str(e))
            self.failed_calls += 1
