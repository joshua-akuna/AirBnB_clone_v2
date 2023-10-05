# Puppet configuration manifest for servers

package {'nginx':
  ensure => installed,
}

file {'/data':
  ensure => directory,
}

file {'/data/web_static':
  ensure => directory,
}

file {'/data/web_static/releases':
  ensure => directory,
}

file {'/data/web_static/shared':
  ensure => directory,
}

file {'/data/web_static/releases/test':
  ensure => directory,
}

file {'/data/web_static/releases/test/index.html':
  ensure  => file,
  content => "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>",
}

file {'/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
}

exec {'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/',
}

exec {'config':
  provider => shell,
  command  => 'sudo sed -i "s/server_name _;/server_name _;\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t\tautoindex off;\n\t}/" /etc/nginx/sites-available/default'
}

exec {'restart':
  provider => shell,
  command  => "sudo service nginx restart"
}
