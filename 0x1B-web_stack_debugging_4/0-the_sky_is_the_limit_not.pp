# increase nginx file limit

exec {'increase':
command => "/bin/sed -i 's/15/6024/' /etc/default/nginx",
}

exec { 'restart':
command => '/usr/sbin/service nginx restart',
require => 'Exec[increase]',
}
