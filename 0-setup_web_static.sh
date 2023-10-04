#!/usr/bin/env bash
#

if ! command -V nginx &> /dev/null
then
	# sudo apt-get update
	# sudo apt-get install nginx
	echo "installing" # TO BE DELETED
fi

mkdir -p data/web_static/releases/test/
mkdir -p data/web_static/shared
echo "<html>
	<head></head>
	<body>
		Holberton School
	</body>
</html>" > data/web_static/releases/test/index.html

if [[ -L "/data/web_static/current" ]]
then
	echo "SYMLINK EXISTS"
fi

ln -sf  data/web_static/releases/test data/web_static/current

ls -l data # TO DELETE
chown -R ubuntu:ubuntu data
ls -l data # TO DELETE
