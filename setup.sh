#!/bin/sh
sudo apt-get install software-properties-common
sudo curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs
sudo apt-get install python3-pip
python3 -m pip install -U discord.py
pip install libnacl
sudo apt install python3.8-venv
python3 -m venv bot-env
pip install -r requirements.txt
export PYTHONPATH="${PYTHONPATH}:discordBot"
sudo apt install ffmpeg
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo npm i -g pm2

echo "Clonar repo, git lfs install, git lfs fetch --all, env file"