from apex_legends_voicelines import __version__
from apex_legends_voicelines import __main__ as m


def test_version():
    assert __version__ == "0.1.0"


legends = {
    "foo": {"name": "Foo", "intro": ["Line 1",],},
    "bar": {"celebrations": ["Line 2",], "name": "Bar",},
}


def test_voice_lines_list():
    expected = [
        "Line 1 - Foo",
        "Line 2 - Bar",
    ]
    voice_lines = m.create_voice_lines(legends)
    assert voice_lines == expected


def test_voice_lines_wraith():
    expected = [
        "Line 2 - Bar",
    ]
    voice_lines = m.create_voice_lines(legends, ["bar"])
    assert voice_lines == expected


def test_check_name_in_list_1():
    assert m.check_name_in_list("foo", None) is True


def test_check_name_in_list_2():
    assert m.check_name_in_list("foo", ["foo"]) is True


def test_check_name_in_list_3():
    assert m.check_name_in_list("foo", ["bar"]) is False


def test_append_name():
    expected = ["Line 1 - Foo", "Line 2 - Foo"]
    input_list = ["Line 1", "Line 2"]
    assert m.append_name_to_lines(input_list, "Foo") == expected
