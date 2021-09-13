from sample_app.tasks import sample_heavy_task

def test_bg_task(transactional_db, broker, worker):
	sample_heavy_task.send()

