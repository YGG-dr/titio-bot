from __future__ import annotations
import logging, os, sys
from dotenv import load_dotenv

class Environment:
	def __init__(self, required: tuple[str,...]=('ENV',)): self._required=required
	def load(self)-> None: load_dotenv()
	def is_dev(self)-> bool: return os.getenv('ENV')=='dev'
	def validate(self)-> None:
		missing:list[str]=[v for v in self._required if not os.getenv(v)]
		if missing: raise RuntimeError(f"Missing env vars: {', '.join(missing)}")

class Logger:
	@staticmethod
	def setup(is_dev: bool)-> None:
		logging.basicConfig(
			level=logging.DEBUG if is_dev else logging.INFO,
			format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
			datefmt="%Y-%m-%d %H:%M:%S",
		)

class App:
	def __init__(self)-> None:
		self._env=Environment()
		self._log:logging.Logger|None=None

	def bootstrap(self)-> None:
		self._env.load(); self._env.validate()
		Logger.setup(self._env.is_dev())
		self._log=logging.getLogger('app')

	def run(self)-> None:
		self._log.info('P.S Started!')

	def shutdown(self, exc:Exception|None=None)-> int:
		if exc: self._log.exception('Fatal error!')
		if exc and self._env.is_dev(): raise exc
		return 1 if exc else 0

def main()-> None:
	app=App()
	try: app.bootstrap(); app.run()
	except Exception as exc: code=app.shutdown(exc)
	else: code=app.shutdown()
	sys.exit(code)

if __name__=='__main__': main()
