.PHONY: env tests reproduce paper

env:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

tests:
	pytest -q

reproduce:
	python scripts/reproduce.py --config config/example.json

paper:
	cd paper && make

