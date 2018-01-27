#!/usr/bin/env bash

set -e

sudo apt-add-repository -y ppa:ansible/ansible
sudo apt-get update -qq
sudo apt-get install -qq build-essential gettext python-dev zlib1g-dev libpq-dev
xvfb libtiff4-dev libjpeg8-dev libfreetype6-dev liblcms1-dev libwebp-dev libtiff4-dev
libjpeg8-dev libfreetype6-dev liblcms1-dev libwebp-dev graphviz-dev firefox automake
libtool libreadline6 libreadline6-dev libreadline-dev libsqlite3-dev libxml2 libxml2-dev
libssl-dev libbz2-dev wget curl llvm python-setuptools python3-dev python-virtualenv
python-pip software-properties-common ansible

#- ansible-galaxy install thefinn93.letsencrypt
#- echo ${VAULT_PASSWORD_KEY} | gpg --passphrase-fd 0 .vault_password.txt.gpg
#- ansible-vault decrypt travis_rsa.vault --output travis_rsa.key
#- mv travis_rsa.key ~/.ssh/travis_rsa

sudo apt-get -y -o Dpkg::Options::="--force-confnew" install docker-ce
sudo rm /usr/local/bin/docker-compose
curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` > docker-compose
chmod +x docker-compose
sudo mv docker-compose /usr/local/bin
sudo service redis-server start


