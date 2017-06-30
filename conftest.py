from data import test_cases

def pytest_generate_tests(metafunc):
    """
    This method is automatically found by pytest and used to parametrize the test cases in test_mms_single_device.py.
    It also has the logic for deciding which resource pool to get account and preset data from (based on argument passed from Jenkins).
    """
    idlist = []
    test_data = []
    fixture_name = ''

    for name, tests in test_cases.items():
        if name.lower() in metafunc.funcargnames:
            fixture_name = name.lower()
            for item in tests:
                idlist.append(item['test_id'])
            test_data = tests
    metafunc.parametrize(fixture_name, test_data, ids=idlist)