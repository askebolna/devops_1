#!/bin/bash

if [ ! -f .env ]; then
	cp .env.example .env
fi

echo "Запуск контейнеров..."
sudo docker compose up -d --build --wait

echo -e "\nПроверка доступности nginx"
curl -v http://localhost

echo -e "\n\nПроверка изоляции backend"
curl --connect-timeout 2 http://localhost:8080
