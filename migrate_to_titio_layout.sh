#!/bin/sh
set -e

echo "==> Criando estrutura titio-bot..."

mkdir -p \
	titio-bot-discord \
	titio-core \
	titio-commons \
	titio-adapters \
	titio-infra \
	resources

echo "==> Movendo bot -> titio-bot-discord"
mv bot/* titio-bot-discord/
rmdir bot

echo "==> Movendo core -> titio-core"
mv core/* titio-core/
rmdir core

echo "==> Movendo commons -> titio-commons"
mv commons/* titio-commons/
rmdir commons

echo "==> Movendo adapters -> titio-adapters"
mv adapters/* titio-adapters/
rmdir adapters

echo "==> Movendo infra -> titio-infra"
mv infra/* titio-infra/
rmdir infra

echo "==> Criando __init__.py raiz (segurança)"
touch \
	titio-bot-discord/__init__.py \
	titio-core/__init__.py \
	titio-commons/__init__.py \
	titio-adapters/__init__.py \
	titio-infra/__init__.py

echo "==> Migração estrutural concluída ^~^"
