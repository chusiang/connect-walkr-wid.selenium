.PHONY: main install update freeze run clean

main: run

install_virtualenv:
	-sudo easy_install virtualenv

init:
	-virtualenv --no-site-packages .venv
	( \
		. .venv/bin/activate; \
		pip install selenium; \
	)

update:
	( \
		. .venv/bin/activate; \
		pip install --upgrade pip; \
		pip install --upgrade -r requirement.txt; \
	)

freeze:
	( \
		. .venv/bin/activate; \
		pip freeze > requirement.txt; \
	)

run:
	( \
		. .venv/bin/activate; \
		python play.py; \
	)

clean:
	rm -rf .venv/

