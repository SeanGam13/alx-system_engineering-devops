# This script installs a package titled 'puppet-lint'
package {'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gem',
}