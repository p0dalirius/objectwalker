.PHONY : all clean docs uninstall install tests build upload

all: clean uninstall install

clean:
	@rm -rf `find ./ -type d -name "*__pycache__"`
	@rm -rf ./build/ ./dist/ ./objectwalker.egg-info/

docs:
	@python3 -m pip install pdoc
	@echo "[$(shell date)] Generating docs ..."
	@python3 -m pdoc -d markdown -o ./documentation/ ./objectwalker/
	@echo "[$(shell date)] Done!"

uninstall:
	@python3 -m pip uninstall objectwalker --yes --break-system-packages

install: uninstall build
	@python3 setup.py install

tests: build
	@python3 ./objectwalker/tests/start_tests.py

build:
	@python3 setup.py sdist bdist_wheel

upload: clean build
	@twine upload dist/*
