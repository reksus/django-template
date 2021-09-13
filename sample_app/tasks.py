import dramatiq
import logging
import time

logging.basicConfig(level=logging.INFO)
logging.getLogger("pika").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

@dramatiq.actor
def sample_heavy_task():
	# what each log level is used for
	logger.debug("Low level system information for debugging purposes")
	logger.info("General system information")
	logger.warning("Information describing a minor problem that has occurred.")
	logger.error("Information describing a major problem that has occurred.")
	logger.critical("Information describing a critical problem that has occurred.")

	# # logs for this sample_heavy_task
	# logger.info("sample heavy completing in 5 seconds")
	# time.sleep(5)
	logger.info("sample heavy task completed.")
