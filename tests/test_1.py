import allure


@allure.epic("estimateme-probation")
@allure.feature("Проверка формирования отчета Allure")
class TestOk:
    """Проверка формирования отчета Allure"""

    @allure.suite("Проверка формирования отчета Allure")
    @allure.title("Проверка формирования отчета Allure")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_ok(self):
        assert True
