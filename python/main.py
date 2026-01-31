from __future__ import annotations
import logging, os, sys
from typing import Final
from dotenv import load_dotenv

class Environment:
	REQUIRED: Final[tuple[str,...]]=('ENV',)
	@staticmethod
	def load()-> None: load_dotenv()
	@staticmethod
	def is_dev()-> bool:return os.getenv('ENV') == 'dev'
	@staticmethod
	def validate()-> None:
		missing: list[str] = [v for v in Environment.REQUIRED if not os.getenv(v)]
		if missing:raise RuntimeError(f"Missing env vars: {', '.join(missing)}")

class Logger:
	@staticmethod
	def setup()-> None:
		logging.basicConfig(
			level = logging.DEBUG if Environment.is_dev() else logging.INFO,
			format = "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
			datefmt = "%Y-%m-%d %H:%M:%S",
		)

class App:
	def __init__(self)-> None: self._log:logging.Logger = logging.getLogger('App')
	def bootstrap(self)-> None: Environment.load(); Environment.validate(); Logger.setup()
	def run(self)-> None: self._log.info('P.S Started!')
	def shutdown(self, exc:Exception|None=None)-> None:
		if exc:self._log.exception('Fatal error!')
		if exc and Environment.is_dev(): raise exc
		sys.exit(1 if exc else 0)

def main()-> None:
	app: App=App()
	try: app.bootstrap(); app.run()
	except Exception as exc: app.shutdown(exc)
	else: app.shutdown()

if __name__=='__main__': main()
