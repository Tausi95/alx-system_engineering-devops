file { '/var/www/html/':
  ensure  => 'directory',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}

