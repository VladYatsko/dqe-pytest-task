import allure


@allure.suite('hr.locations test suite')
class TestLocations:
    @allure.title('MAX value validation for street_address field')
    def test_max_value(self, database_connection):
        with allure.step('Specify as query and execute'):
            query = database_connection.execute("SELECT MAX(street_address) FROM hr.locations").fetchall()
        
        with allure.step('Validation that MAX value matches expected from source'):
            expected_result = [('Schwanthalerstr. 7031',)]
            assert str(query) == str(expected_result), f"Expected: {expected_result}, Actual: {query}"
    
    @allure.title('Validation that user is able to put proper data to database')
    def test_insertion_of_data(self, database_connection):
        with allure.step('Get actual size of DB.'):
            query = database_connection.execute("SELECT * FROM hr.locations").fetchall()
        
        with allure.step('Insert data to the database'):
            database_connection.execute("INSERT INTO hr.locations (street_address, postal_code, "
                                        "city, state_province, country_id)"
                                        "VALUES ('Some street 10', 'MS13A', 'Brest', 'Belarus', 'UK')")
            database_connection.commit()
            with allure.step('Save the size of DB'):
                old_size = len(query)
        
        with allure.step('Get the updated DB size'):
            query = database_connection.execute("SELECT * FROM hr.locations").fetchall()
            with allure.step('Save updated size to variable'):
                new_size = len(query)
        
        with allure.step('Check that size was incremented by 1'):
            assert new_size == old_size + 1
