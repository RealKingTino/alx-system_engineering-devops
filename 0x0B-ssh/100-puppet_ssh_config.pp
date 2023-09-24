# Setting up client config file
include stdlib

file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  ensure  => 'present',
  replace => true,
}

file_line { 'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  ensure  => 'present',
  replace => true,
}
