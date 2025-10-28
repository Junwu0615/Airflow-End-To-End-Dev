from lib.etl_processor import ETLProcessor

def test_transform():
    res = ETLProcessor.transform(10)
    assert res["original"] == 10
    assert res["doubled"] == 20