from ci_cd_ai_service.calculator import add


def test_add():
    assert add(2,3) == 5
    