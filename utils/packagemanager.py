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
        if not os.path.exists(PACKAGE_DIR):
            os.mkdir(PACKAGE_DIR)
        os.chdir(PACKAGE_DIR)
        print(f"Start to download {package_name}.")
        timestamp_bef = round(time.time() * 1000)
        try:
            response = get(content["pkg_source"], allow_redirects=True, stream=True)
        except:
            print("Download failed.")
            return False
        timestamp_aft = round(time.time() * 1000)
        delta_time = timestamp_aft - timestamp_bef
        print(f"Downloaded successfully. It took {delta_time/1000} seconds.")
        with open(content["local_file_name"], "wb") as f:
            f.write(response.content)
            f.close()
        return True
    else:
        return False

def update_source(environment, package_source, package_name):
    PACKAGE_CACHE = environment + os.sep + "cache" + os.sep + "packagemanager" + os.sep + package_name + ".json"
    print(f"Start to delete {PACKAGE_CACHE}")
    os.remove(PACKAGE_CACHE)
    print(f"Deleted successfully. Start to update {package_name}")
    if not get_source(environment,package_source,package_name):
        print("Update failed.")
        return False
    try:
        if install_pkg(environment, package_name):
            print("Updated successfully.")
            return True
        else:
            return False
    except:
        print("Update failed.")
        return False

def get_source(environment, package_source, package_name):
    PACKAGE_CACHE = environment + os.sep + "cache" + os.sep + "packagemanager" + os.sep + package_name + ".json"
    print(f"Start to download the source of {package_name}")
    try:
        response = get(package_source, allow_redirects=True, stream=True)
    except:
        print("Download failed.")
        return False
    with open(PACKAGE_CACHE, "wb") as f:
        f.write(response.content)
        f.close()
    return True
if __name__ == "__main__":
    get_source(environment=r"C:\Users\MeteorOfTime\Documents\GitHub\mterminal", package_source=r"https://raw.githubusercontent.com/MeteorOfTime/mterminal/main/cache/packagemanager/test1.json", package_name="test1")
    update_source(environment=r"C:\Users\MeteorOfTime\Documents\GitHub\mterminal", package_source=r"https://raw.githubusercontent.com/MeteorOfTime/mterminal/main/cache/packagemanager/test1.json", package_name="test1")