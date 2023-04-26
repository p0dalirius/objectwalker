.PHONY : all clean build upload

all: install clean

clean:
	@rm -rf `find ./ -type d -name "*__pycache__"`
	@rm -rf ./build/ ./dist/ ./objectwalker.egg-info/

docs:
	@python3 -m pip install pdoc
	@echo "[$(shell date)] Generating docs ..."
	@python3 -m pdoc -d markdown -o ./documentation/ ./objectwalker/
	@echo "[$(shell date)] Done!"

install: build
	python3 -m pip uninstall objectwalker --yes
	python3 setup.py install

build:
	python3 setup.py sdist bdist_wheel

upload: build
	twine upload dist/*