.PHONY: up
up:
	sudo docker-compose up -d

.PHONY: down
down:
	sudo docker-compose down

.PHONY: logs
logs:
	sudo docker-compose logs -f

.PHONY: build
build:
	sudo docker build -t deadline_telegram_bot .

.PHONY: config
config:
	cp config/config.example.yml config/config.yml