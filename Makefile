.PHONY: install test run

install:
	poetry install

test:
	poetry run pytest tests/test.py

run:
	poetry run python src/app.py

lint:
	poetry run flake8 src

amend-and-push:
	git add .
	git commit --amend --no-edit
	git push --force

say-hello:
	@echo "Hello, World!"