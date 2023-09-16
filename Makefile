args := $(wordlist 2, 100, $(MAKECMDGOALS))

env:
	cp .env.example .env

run:
	python3 -m poetry run python3 -m app

revision: 
	cd app/db; python3 -m poetry run alembic revision --autogenerate

upgrade:
	cd app/db; python3 -m poetry run alembic upgrade $(args)

up:
	docker compose up -d --remove-orphans
	
down:
	docker compose down