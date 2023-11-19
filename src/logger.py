from loguru import logger


logger.add('app.log', format="{time} {level} {message}")
