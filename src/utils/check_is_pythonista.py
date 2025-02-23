import os
import plistlib
import sys

def check_is_pythonista():
    try:
        with open(os.path.abspath(os.path.join(sys.executable, '..', 'Info.plist')), 'rb') as f:
            plist = plistlib.load(f)

        # return the CFBundleIdentifier from the plist
        bundle_identifier = '{CFBundleIdentifier}'.format(**plist)
        return 'com.omz-software.Pythonista' in bundle_identifier

    except:
        return False
