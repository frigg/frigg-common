help:
	@echo "test - run this often"

isort:
	isort -rc frigg tests

test:
	flake8
	tox
	coverage combine
	coverage html
	open htmlcov/index.html
