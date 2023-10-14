import sys

for path in sys.path:
    print(path)

import site
print(site.getsitepackages())
