# execute a command to kill process killmenow

exec {'killmenow':
  command => '/usr/bin/pkill killmenow'
}
