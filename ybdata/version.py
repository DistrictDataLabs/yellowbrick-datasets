# ybdata.version
# Maintains version and package information for deployment.
#
# Author:   Benjamin Bengfort <bbengfort@districtdatalabs.com>
# Created:  Sun Dec 30 08:49:55 2018 -0500
#
# For license information, see LICENSE.txt
#
# ID: version.py [] benjamin@bengfort.com $

"""
Maintains version and package information for deployment.
"""

##########################################################################
## Module Info
##########################################################################

__version_info__ = {
    'major': 1,
    'minor': 0,
    'micro': 0,
    'releaselevel': 'final',
    'serial': 1,
}

##########################################################################
## Helper Functions
##########################################################################

def get_version(short=False):
    """
    Prints the version.
    """
    assert __version_info__['releaselevel'] in ('alpha', 'beta', 'final')
    vers = ["%(major)i.%(minor)i" % __version_info__, ]
    if __version_info__['micro']:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__['releaselevel'] != 'final' and not short:
        vers.append('%s%i' % (__version_info__['releaselevel'][0],
                              __version_info__['serial']))
    return ''.join(vers)
