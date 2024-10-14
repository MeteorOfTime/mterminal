from requests import get
import os
import json
import shutil


def install_pkg(environment, package_name):
    PACKAGE_DIR = environment+os.sep+"packages"+os.sep+package_name
    PACKAGE_CACHE = environment+os.sep+"cache"+os.sep+"packagemanager"+os.sep+package_name+".json"
    with open(PACKAGE_CACHE,"r", encoding="utf-8") as j:
        content = json.load(j)
        j.close()
    if os.path.exists(PACKAGE_DIR):
        shutil.rmtree(PACKAGE_DIR)
    os.mkdir(PACKAGE_DIR)
    os.chdir(PACKAGE_DIR)
    response = get(content["pkg_source"], allow_redirects=True, stream=True)
    with open(content["local_file_name"], "wb") as f:
        f.write(response.content)
        f.close()

if __name__ == "__main__":
    install_pkg(environment=r"C:\Users\MeteorOfTime\Documents\GitHub\mterminal", package_name="test")