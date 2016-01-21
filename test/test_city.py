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
        
    def test_build_config_path(self):
        city = City()
        assert City.build_config_path("test") == "../config/city/test.json"
        
    def test_build_output_path(self):
        city = City()
        assert City.build_output_path("test") == "../output/city/test.json"
        
    def test_build_dict_name(self):
        city = City()
        city.name = "test"
        
        city_dict = city.build_dictionary()
        assert city_dict["name"] == "test"
        
    def test_build_dict_pop(self):
        city = City()
        city.population = 100
        
        city_dict = city.build_dictionary()
        assert city_dict["population"] == 100
    
    def test_build_dict_race(self):
        city = City()
        city.race_relation = "good"
        
        city_dict = city.build_dictionary()
        assert city_dict["race relation"] == "good"
    
    def test_build_dict_ruler(self):
        city = City()
        city.ruler_status = "just"
        
        city_dict = city.build_dictionary()
        assert city_dict["ruler status"] == "just"
        
    def test_build_dict_trait(self):
        city = City()
        city.notable_trait = "river"
        
        city_dict = city.build_dictionary()
        assert city_dict["notable trait"] == "river"
        
    def test_build_dict_known(self):
        city = City()
        city.known_for = "food"
        
        city_dict = city.build_dictionary()
        assert city_dict["known for"] == "food"
    
    def test_build_dict_calamity(self):
        city = City()
        city.calamity = "doom"
        
        city_dict = city.build_dictionary()
        assert city_dict["calamity"] == "doom"
    
    # Test save_to_file()
    
    # Test build_random()
        
        
        
        
        
        
        
        
        
    
    