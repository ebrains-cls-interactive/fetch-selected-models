
clean:
	rm -rf dist *.egg-info

build:
	which python3
	python3 setup.py sdist
