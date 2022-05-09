import os
import yaml
import json
from features.businesslogic.Authentication import ValidateAuthentication
obj_ValidateAuthentication = ValidateAuthentication()

class ValidateApiResponse:
    list_symbols_ids = []
    info_obj_response = ""

    def get_api_ids(self,pstr_endpoint,pstr_symbols):
        """
        Description:
        |  This method takes endpoints and symbols, make the api call and gets ids in response
        """
        try:
            endpoint = pstr_endpoint
            list_symbols = pstr_symbols.split(",")
            config_load = self.read_base_config_file()
            url = config_load['environment']
            url = url + endpoint
            api_key = config_load['api_key']

            self.obj_response = obj_ValidateAuthentication.get_api_connection(url, api_key)

            for symbols in list_symbols:
                for line in self.obj_response['data']:
                    if symbols == line["symbol"]:
                        self.list_symbols_ids.append(line["id"])
                        break

            if self.list_symbols_ids.__len__() == 3:
                return True
            else:
                return False
        except Exception as e:
            print("Error in get_api_ids method-->" + str(e))
            return None

    def get_api_info(self,pstr_endpoint,pstr_symbols):
        """
        Description:
        |  This method takes endpoints and symbols, make the api call and gets currency information in response
        """
        try:
            endpoint = pstr_endpoint
            list_symbols = pstr_symbols.split(",")
            config_load = self.read_base_config_file()
            url = config_load['environment']
            url = url + endpoint
            api_key = config_load['api_key']
            parameters = {
                'symbol': pstr_symbols
            }
            self.info_obj_response = obj_ValidateAuthentication.get_api_connection(url, api_key, parameters=parameters)

            if self.info_obj_response is not None:
                return True
            else:
                return False
        except Exception as e:
            print("Error in get_api_ids method-->" + str(e))
            return None

    def get_api_info_provided(self,pstr_endpoint,pint_numbers):
        """
        Description:
        |  This method takes endpoints and numbers of currency ids comma seperated, make the api call and gets information of provided ids in response
        """
        try:
            endpoint = pstr_endpoint
            number = pint_numbers
            config_load = self.read_base_config_file()
            url = config_load['environment']
            url = url + endpoint
            api_key = config_load['api_key']
            parameters = {
                'id': number
            }
            self.info_obj_response = obj_ValidateAuthentication.get_api_connection(url, api_key, parameters=parameters)

            if self.info_obj_response is not None:
                return True
            else:
                return False
        except Exception as e:
            print("Error in get_api_ids method-->" + str(e))
            return None

    def price_conversion(self,pstr_currency, pstr_endpoint):
        """
        Description:
        |  This method takes endpoints and currency, make the api call and gets converted currencies in response
        """
        try:
            endpoint = pstr_endpoint
            currency = pstr_currency

            config_load = self.read_base_config_file()
            url = config_load['environment']
            url = url + endpoint
            api_key = config_load['api_key']

            for ids in self.list_symbols_ids:
                parameters = {
                    'id': ids,
                    'amount': 1,
                    'convert': currency
                }
                self.obj_response = obj_ValidateAuthentication.get_api_connection(url, api_key, parameters=parameters)
                print("convert currency:" + self.obj_response['data']['name'] + " to currency: " + currency + " and Price is " + str(self.obj_response['data']['quote']['BOB']['price']))
        except Exception as e:
            print("Error in price_conversion method-->" + str(e))

    def get_data_and_validate(self, pstr_jsonfile):
        """
        Description:
            |  This method gets the input data from Json file and validate it with the api response

        """
        try:
            obj_json_path = Path = os.getcwd() + os.path.sep + r"features\testdata" + os.path.sep + pstr_jsonfile
            with open(obj_json_path) as obj_data:
                obj_json_data = json.load(obj_data)
            IsValidated = True

            if self.info_obj_response['data']['ETH']['logo'] != obj_json_data['logo']:
                return False
            if self.info_obj_response['data']['ETH']['symbol'] != obj_json_data['symbol']:
                return False
            if self.info_obj_response['data']['ETH']['date_added'] != obj_json_data['date_added']:
                return False
            if self.info_obj_response['data']['ETH']['urls']['technical_doc'][0] != obj_json_data['technical_doc']:
                return False
            for x in self.info_obj_response['data']['ETH']['tags']:
                if x == obj_json_data['tags']:
                    IsValidated = True
                    break
                else:
                    IsValidated = False
            return IsValidated

        except Exception as ex:
            self.__obj_generic_exception.raise_custom_exception(str(ex))
            return False

    def get_associated_tag_and_validate(self, pstr_tags):
        """
        Description:
        |  This method takes associated tags and validate it with the response
        """
        try:
            for line in self.info_obj_response['data']:
                for x in self.info_obj_response['data'][line]['tags']:
                    if x == pstr_tags:
                        print("id" + str(self.info_obj_response['data'][line]['id']) + "is associated with" + pstr_tags)
                        break
        except Exception as ex:
            self.__obj_generic_exception.raise_custom_exception(str(ex))
            return False

    def read_base_config_file(self):
        """
        Description:
            |  This method reads base config.yml file and loads the content into a dictionary object.

        """
        try:
            count = 0
            config = None
            while config is None and count < 30:
                try:
                    Path = os.getcwd() + os.path.sep + "config.yml"
                    with open(Path, 'r') as config_yml:
                        config = yaml.load(config_yml)
                except Exception as e:
                    pass
                count = count + 1
            if config is None:
                raise Exception("Error Occurred while reading a config file")
            return config
        except Exception as e:
            print("Error in read_base_config_file method-->" + str(e))
            return None


