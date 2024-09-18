# Including commands
run-django-server:
	poetry run task manage runserver

run-quasar-server:
	yarn quasar dev

install-backend:
	poetry install --with dev --no-root

install-backend-prod:
	poetry install --with prod --no-root

install-frontend:
	yarn install

.PHONY: run-frontend
run-frontend:
	@make run-quasar-server

.PHONY: run-backend
run-backend:
	@make run-django-server

.PHONY: clear
clear:
	poetry run task clear

.PHONY: createadmin
createadmin:
	poetry run task createsuperuser

.PHONY: migrate
migrate:
	poetry run task migrate

# Primary commands
.PHONY: install
install:
	@make -j 2 install-backend install-frontend
	poetry run task initconfig --debug
	@make migrate
	poetry run task defaultadmin
	poetry run task defaultfixtures

.PHONY: install-prod
install-prod:
	poetry run pip install -U pip
	@make install-backend-prod
	poetry run task initconfig

.PHONY: run
run:
	@make -j 2 run-django-server run-quasar-server

.PHONY: build
build:
	poetry run task collectstatic
	@make migrate
	poetry run task defaultadmin
	poetry run task defaultfixtures
