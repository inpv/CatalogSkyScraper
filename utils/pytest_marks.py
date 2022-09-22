import pytest
import allure

# web browser
browser = pytest.mark.usefixtures("browser")

# allure report
title = allure.title
