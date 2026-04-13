import pytest
import allure
from ups_flashing import ups_flashing


@allure.feature("UPS Firmware")
@allure.story("UPS flashing validation")
@pytest.mark.flash
def test_ups_flashing():

    result = ups_flashing()

    # Firmware Version
    allure.attach(
        result["fw_version"],
        name="Firmware Version",
        attachment_type=allure.attachment_type.TEXT
    )

    # Hardware Revision
    allure.attach(
        result["hw_revision"],
        name="Hardware Revision",
        attachment_type=allure.attachment_type.TEXT
    )

    # Flashing Time
    allure.attach(
        result["time"],
        name="Flashing Time",
        attachment_type=allure.attachment_type.TEXT
    )

    # Logs
    allure.attach(
        result["log"],
        name="Flashing Log",
        attachment_type=allure.attachment_type.TEXT
    )

    allure.dynamic.title(
        f"UPS Flash - {result['fw_version']} | {result['hw_revision']}"
    )

    assert result["status"], "UPS flashing failed"