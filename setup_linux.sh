#!/bin/bash
sudo apt update
sudo apt install -y python3-tk python3-pil.imagetk
pip install -r requirements.txt --break-system-packages
echo "Все зависимости успешно установлены!"
