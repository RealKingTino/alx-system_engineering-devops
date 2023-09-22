# kill process killnow

exec { 'pkill':
  command     => '/usr/bin/pkill killmenow',
}
