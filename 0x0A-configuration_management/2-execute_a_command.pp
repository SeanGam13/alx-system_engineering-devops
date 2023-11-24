# This script executes a command titled 'pkill killmenow'
exec { 'pkill killmenow':
  path => '/usr/bin:/usr/sbin:/bin'
}