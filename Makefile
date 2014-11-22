help:
	@echo "test - run this often"

test:
	flake8
	tox
	coverage combine
	coverage html
	open htmlcov/index.html
