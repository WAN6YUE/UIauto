import pytest
import os

if __name__ == "__main__":
    # pytest.main(["--alluredir=./temp/my_allure_results"])   #程序入口
    pytest.main()
    os.system("allure serve ./temp/my_allure_results")

