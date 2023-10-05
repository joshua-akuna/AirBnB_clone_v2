#!/usr/bin/env bash
#

if ! command -V nginx &> /dev/null
then
	sudo apt-get update
	sudo apt-get install nginx
fi

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared
echo "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>" | sudo tee /data/web_static/releases/test/index.html >& /dev/null

sudo ln -sf  /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

config_file="/etc/nginx/sites-available/default"
replacement="server_name _;\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t\tautoindex off;\n\t}"
sudo sed -i "s/server_name _;/$replacement/" "$config_file"

sudo service nginx restart
