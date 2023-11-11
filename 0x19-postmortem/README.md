# Web Stack Debugging Project Postmortem

## Issue Summary
On Nov 6, 2023, at 6:00 AM Nigeria time, an outage occurred on an isolated Ubuntu 14.04 container running an Apache web server. GET requests on the server led to 500 Internal Server Error’s, when the expected response was an HTML file defining a simple Holberton WordPress site. The outage lasted for about 30 minutes, until the root cause was identified and fixed. The impact of the outage was moderate, as it affected about 10% of the users who were trying to access the WordPress site.

# Debugging Process
The issue was detected by a monitoring alert that notified the web stack debugging team of a spike in 5xx errors on the server. The team followed these steps to investigate and resolve the issue:
* Checked the Apache error log and found the following message: PHP Fatal error:  Unknown: Failed opening required '/var/www/html/wp-settings.php' (include_path='.:/usr/share/php:/usr/share/pear') in Unknown on line 0
* Checked the /var/www/html/wp-settings.php file and found that it had a typo in the file extension: phpp instead of php.
* Corrected the typo and restarted the Apache service.
* Verified that the WordPress site was working as expected and the 500 errors were gone.

# Root Cause and Resolution
The root cause of the issue was a human error that introduced a typo in the '/var/www/html/wp-settings.php' file. The typo caused the PHP interpreter to fail to load the file, resulting in a fatal error and a 500 response code. The resolution was to fix the typo and restart the Apache service.

# Corrective and Preventive Measures
To prevent this issue from happening again, the following measures are recommended:
1. Implement a code review process for any changes to the WordPress files, to catch any typos or syntax errors before deploying them to the server.
2. Add a unit test or a smoke test for the WordPress site, to ensure that it can load the wp-settings.php file and return a 200 response code.
3. Use a configuration management tool, such as Puppet, to automate the deployment of the WordPress files and ensure consistency across the servers. The following Puppet manifest can be used to fix any bad phpp extensions to php in the WordPress file 'wp-settings.php:'

# Fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`.

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

