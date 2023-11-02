################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          <  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         / / 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / /  
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_/   
#                                                                        
#  Question 1
################################################################################
#
# Instructions:
# The two functions below are used to tell the weather. They have some bugs that
# need to be fixed. The test suite in `question1_test.py` will verify the output.
# Read the test suite to know the values that these functions should return.

city_options = {
   "Quito": {"temperature": 22, "weather": "sunny"},
   "Sao Paulo": {"temperature": 17, "weather": "cloudy"},
   "San Francisco": {"temperature": 16, "weather": "partly cloudy"},
   "New York": {"temperature": 14, "weather": "rainy"}
}

def get_city_temperature(city):

   resp = city_options.get(city)
   return resp["temperature"]

def get_city_weather(city):

  resp = city_options.get(city)
  return str(resp["temperature"]) + " degrees and " + resp["weather"]
