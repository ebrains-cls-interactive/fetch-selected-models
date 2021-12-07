
clean:
	rm -rf dist *.egg-info

build:
	which python3
	python3 setup.py sdist

test_local:
	cd test && cd CLS-INTERACTIVE-UC && python3 test-morph.py