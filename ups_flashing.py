import subprocess
from datetime import datetime

UNIFLASH_PATH = "/home/vvdn/ti/uniflash_9.5.0/deskdb/content/TICloudAgent/linux/ccs_base/DebugServer/bin/DSLite"
CONFIG_PATH = "/home/vvdn/target.ccxml"
FW_PATH = "/home/vvdn/Downloads/BCI_POC_Board_v0_0_6.out"


def get_fw_version():
    version = FW_PATH.split("_v")[-1].replace(".out", "")
    return f"FV_{version}"


def get_hw_revision():
    return "HW_REV_A1"


def ups_flashing():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fw_version = get_fw_version()
    hw_revision = get_hw_revision()

    cmd = [
        UNIFLASH_PATH,
        "flash",
        f"--config={CONFIG_PATH}",
        "--flash",
        "--verbose",
        FW_PATH
    ]

    result = subprocess.run(cmd, text=True, capture_output=True)

    return {
        "status": result.returncode == 0,
        "log": result.stdout,
        "time": timestamp,
        "fw_version": fw_version,
        "hw_revision": hw_revision
    }