install:
	poetry install

build:
	poetry build
	
run:
	poetry run src\scripts\draw.py

test:
	poetry run pytest

lint:
	poetry run flake8

format:
	poetry run black .

clean:
	rm -rf .ven

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall
