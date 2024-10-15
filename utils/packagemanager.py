from requests import get
import os
import json
import shutil
import platform
import time



def install_pkg(environment, package_name):
    PACKAGE_DIR = environment+os.sep+"packages"+os.sep+package_name
    PACKAGE_CACHE = environment+os.sep+"cache"+os.sep+"packagemanager"+os.sep+package_name+".json"
    with open(PACKAGE_CACHE,"r", encoding="utf-8") as j:
        content = json.load(j)
        j.close()
    if content["required_platform"][0] == platform.system() and platform.machine() in content["required_platform"][1]:
        if os.path.exists(PACKAGE_DIR):
            shutil.rmtree(PACKAGE_DIR)
        os.mkdir(PACKAGE_DIR)
        os.chdir(PACKAGE_DIR)
        print("Start to download.")
        timestamp_bef = round(time.time() * 1000)
        response = get(content["pkg_source"], allow_redirects=True, stream=True)
        timestamp_aft = round(time.time() * 1000)
        delta_time = timestamp_aft - timestamp_bef
        print(f"Download successfully. It took {delta_time/1000} seconds.")
        with open(content["local_file_name"], "wb") as f:
            f.write(response.content)
            f.close()
        return True
    else:
        return False

def update_source(environment,package_source):
    PACKAGE_CACHE = environment + os.sep + "cache" + os.sep + "packagemanager" + os.sep + package_name + ".json"


if __name__ == "__main__":
    install_pkg(environment=r"C:\Users\MeteorOfTime\Documents\GitHub\mterminal", package_name="test")
