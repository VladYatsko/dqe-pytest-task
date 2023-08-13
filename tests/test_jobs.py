import allure


@allure.suite("hr.jobs test suite.")
class TestJob:
    @allure.title("Validation that reference integrity is observed between hr.jobs and hr.employees tables")
    def test_reference_integrity(self, database_connection):
        with allure.step('Using left join execute merging hr.jobs to hr.employees'):
            query = database_connection.execute("SELECT e.employee_id, e.first_name, e.last_name, e.job_id, j.job_id, "
                                                "j.job_title FROM hr.employees AS e "
                                                "LEFT JOIN hr.jobs AS j on e.job_id = j.job_id "
                                                "WHERE j.job_id IS NULL OR e.job_id IS NULL").fetchall()
            
        with allure.step('Validation that no NULL values are stored in both tables after joining'):
            assert query == []
            
        with allure.step('Using left join execute merging hr.employees to hr.jobs'):
            query = database_connection.execute("SELECT e.employee_id, e.first_name, e.last_name, e.job_id, j.job_id, "
                                                "j.job_title FROM hr.jobs AS j "
                                                "LEFT JOIN hr.employees AS e on e.job_id = j.job_id "
                                                "WHERE j.job_id IS NULL OR e.job_id IS NULL").fetchall()
            
        with allure.step('Validation that no NULL values are stored in both tables after joining'):
            assert query == []
    
    @allure.title("Validation that salary rules are observed in accordance with min max range")
    def test_salary_rules(self, database_connection):
        with allure.step('Specify as query and execute'):
            query = database_connection.execute('SELECT e.employee_id, e.first_name, e.last_name, e.salary, e.job_id, '
                                                'j.min_salary, j.max_salary FROM hr.employees AS e LEFT JOIN hr.jobs '
                                                'AS j on e.job_id = j.job_id WHERE NOT (e.salary BETWEEN j.min_salary '
                                                'AND j.max_salary);').fetchall()
            
        with allure.step('Validation that salary rules are observed.'):
            assert query == []
