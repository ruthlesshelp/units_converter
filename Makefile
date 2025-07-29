.PHONY: test

test:
	pytest -xv tests

bdd:
	behave --stop
