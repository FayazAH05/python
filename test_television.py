import pytest
from television import Television


def tv() -> Television:
    return Television()


def test_init(tv: Television) -> None:
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_power(tv: Television) -> None:
    """Test the power toggle functionality."""
    tv.power()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"
    tv.power()
    assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"


def test_mute(tv: Television) -> None:
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.power()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"


def test_channel_up(tv: Television) -> None:

    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

    tv.channel = Television.MAX_CHANNEL
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_channel_down(tv: Television) -> None:

    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"
    tv.channel = Television.MIN_CHANNEL
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"


def test_volume_up(tv: Television) -> None:
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.volume = Television.MAX_VOLUME
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"


def test_volume_down(tv: Television) -> None:

    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.volume_down()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.volume_up()
    tv.mute()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"