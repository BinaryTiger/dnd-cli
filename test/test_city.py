import pytest
from workspace.city import City



class TestCity:
    def test_const_extension(self):
        city = City()
        assert city.FILE_EXTENSION != ""
        
    def test_const_config(self):
        city = City()
        assert city.CITY_CONFIG_PATH != ""
        
    def test_const_output(self):
        city = City()
        assert city.OUTPUT_PATH != ""
        
        
    
    