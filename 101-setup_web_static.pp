exec {'update':
  provider => shell,
  command  => "sudo apt-get update -y"
}

exec {'install nginx':
  provider => shell,
  command  => 'sudo apt-get install -y nginx'
}

exec {'create directories':
  provider => shell,
  command  => "sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/",
}

file {'/data/web_static/releases/test/index.html':
  ensure  => present,
  content => "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>
"
}

exec {'create link':
  provider => shell,
  command  => "sudo ln -sf /data/web_static/releases/test /data/web_static/current"
}

exec {'permissions':
  provider => shell,
  command  => "sudo chown -R ubuntu:ubuntu /data/"
}

exec {'config':
  provider => shell,
  command  => 'sudo sed -i "s/server_name _;/server_name _;\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t\tautoindex off;\n\t}/" /etc/nginx/sites-available/default'
}

exec {'restart':
  provider => shell,
  command  => "sudo service nginx restart"
}
