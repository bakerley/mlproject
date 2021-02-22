from mlproject.distance import haversine

def test_type_of_haversine():
    assert type(haversine(48.86713089030775, 2.2962409715114696,2.2962409715114696,48.86713089030775)) == float
