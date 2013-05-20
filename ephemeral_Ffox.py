#! /usr/bin/env python

import subprocess, os, random, string

from twisted.python.filepath import FilePath

basename = os.path.join(os.environ['HOME'], '.mozilla', 'firefox')
profiledir_path = FilePath(basename)

origintemplate_path = profiledir_path.child('templateprofile')

ephemeral_name_prefix = ''.join( random.sample(string.lowercase + string.digits, 8) )
ephemeral_profile_path = profiledir_path.child('%s.ephemeral' % ephemeral_name_prefix)  

origintemplate_path.copyTo(ephemeral_profile_path)

launch_string = 'firefox -no-remote --profile %s' % (ephemeral_profile_path.path,)
retcode = subprocess.call( launch_string.split() )

if retcode != -15:
    ephemeral_profile_path.remove()
