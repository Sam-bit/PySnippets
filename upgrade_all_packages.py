from pkg_resources import working_set
from subprocess import call

packages = [dist.project_name for dist in working_set]
call("python.exe -m pip install --upgrade " + ' '.join(packages), shell=True)
call("winget upgrade --all --accept-package-agreements --accept-source-agreements --include-unknown", shell=True)
call("python.exe -m pip install --upgrade pip", shell=True)
call("python -m pip freeze > .\\requirements.txt", shell=True)
call("winget export -o .\\winget.txt --accept-package-agreements --accept-source-agreements", shell=True)
call("flutter upgrade --force", shell=True)
