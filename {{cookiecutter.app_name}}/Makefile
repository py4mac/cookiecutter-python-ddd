.DEFAULT_GOAL := help

pkg_src = {{cookiecutter.app_name}}
tests_src = tests
docs_src = docs/src
all_src = $(pkg_src) $(tests_src)

isort = isort -rc $(all_src)
autoflake = autoflake -r --remove-all-unused-imports --ignore-init-module-imports $(all_src)
black = black $(all_src)
flake8 = flake8 $(all_src)
mypy_base = mypy --show-error-codes
mypy = $(mypy_base) $(all_src)
test = pytest --cov={{cookiecutter.app_name}}

.PHONY: all  ## Run the most common rules used during development
all: static test

.PHONY: static  ## Perform all static checks (format, lint, mypy)
static: format lint mypy

.PHONY: test  ## Run tests
test:
	$(test)

.PHONY: format  ## Auto-format the source code (isort, autoflake, black)
format:
	$(isort)
	$(autoflake) -i
	$(black)

.PHONY: lint  ## Run flake8 over the application source and tests
lint:
	$(flake8)

.PHONY: mypy  ## Run mypy over the application source and tests
mypy:
	$(mypy)

.PHONY: testcov  ## Run tests, generate a coverage report, and open in browser
testcov:
	$(test)
	@echo "building coverage html"
	@coverage html
	@echo "A coverage report was generated at htmlcov/index.html"
	@if [ "$$(uname -s)" = "Darwin" ]; then \
		open htmlcov/index.html; \
	fi

.PHONY: ci  ## Run all CI validation steps without making any changes to code
ci: test lint mypy check-format

.PHONY: check-format  ## Check the source code format without changes
check-format:
	$(isort) --check-only
	@echo $(autoflake) --check
	@( set -e; $(autoflake) --check | (grep -v "No issues detected!" || true) )
	$(black) --check

.PHONY: clean  ## Remove temporary and cache files/directories
clean:
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -f `find . -type f -name .coverage`
	rm -f `find . -type f -name ".coverage.*"`
	rm -rf `find . -name __pycache__`
	rm -rf `find . -type d -name '*.egg-info' `
	rm -rf `find . -type d -name 'pip-wheel-metadata' `
	rm -rf `find . -type d -name .pytest_cache`
	rm -rf `find . -type d -name .cache`
	rm -rf `find . -type d -name .mypy_cache`
	rm -rf `find . -type d -name htmlcov`
	rm -rf `find . -type d -name "*.egg-info"`
	rm -rf `find . -type d -name build`
	rm -rf `find . -type d -name dist`

.PHONY: db  ## Starting DB
db:
	./scripts/start_db.sh

.PHONY: lock  ## Update the lockfile
lock:
	./scripts/lock.sh

.PHONY: docs-build  ## Generate the docs and update README.md
docs-build:
	mkdocs build
	cp ./docs/index.md ./README.md

.PHONY: docs-format  ## Format the python code that is part of the docs
docs-format:
	isort -rc docs/src
	autoflake -r --remove-all-unused-imports --ignore-init-module-imports docs/src -i
	black -l 82 docs/src

.PHONY: docs-live  ## Serve the docs with live reload as you make changes
docs-live:
	mkdocs serve --dev-addr 0.0.0.0:8008

.PHONY: poetryversion
poetryversion:
	poetry version $(version)

.PHONY: help  ## Display this message
help:
	@grep -E \
		'^.PHONY: .*?## .*$$' $(MAKEFILE_LIST) | \
		sort | \
		awk 'BEGIN {FS = ".PHONY: |## "}; {printf "\033[36m%-16s\033[0m %s\n", $$2, $$3}'