__all__ = (
    "pixel_and_msgb_compatibility",
)


def pixel_and_msgb_compatibility(chanel_value: int, msg_binary: int) -> bool:
    if chanel_value % 2 == 0 and msg_binary == 1 or chanel_value % 2 != 0 and msg_binary == 0:
        return False
    else:
        return True
