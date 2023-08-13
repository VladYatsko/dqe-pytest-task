import allure


@allure.suite('hr.employees test suite.')
class TestEmployees:
    @allure.title("Validation that there are only alphabetical characters for first_name and last_name")
    def test_names_have_only_alphabetical(self, database_connection):
        with allure.step('Specify as query and execute'):
            query = database_connection.execute("SELECT first_name, last_name FROM hr.employees "
                                                "WHERE first_name not like '%[a-zA-Z]%' "
                                                "or last_name not like '%[a-zA-Z]%'").fetchall()
            
        with allure.step('Validation that no data with numbers or special characters is entered'):
            assert query == []
    
    @allure.title("Validation that no duplicates are included into hr.employees table")
    def test_duplicate_check(self, database_connection):
        with (allure.step(' specify as query and execute')):
            query = database_connection.execute(
                'SELECT first_name, last_name, email, COUNT(1) '
                'FROM hr.employees GROUP BY first_name, last_name, email '
                'HAVING COUNT(1) > 1'
            ).fetchall()
            
        with allure.step('Validation that no duplicates are present in table'):
            assert query == []
            