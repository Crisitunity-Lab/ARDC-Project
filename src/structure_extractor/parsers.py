import pycountry
import src.structure_extractor.config as cfg

def parse_label_country(text):
    # Remove the word "ISO" from the string
    text = text.replace("ISO", "")

    country = _get_country_name(text)

    if country == "Country Not Found":
       country = _find_country_name(text)
        
    return country


def _get_country_name(text):
    for country in pycountry.countries:
      # Check if the country name is in the string
      if country.name.lower() in text.lower():
        # If a match is found, return the country name
        country=country.name
      # Check if the country name is an alpha 3 string
      elif country.alpha_3 in text:
        country=country.name
      # Check if the country name is an alpha 2 string
      elif country.alpha_2 in text:
        country=country.name
      else:
        country="Country Not Found"

      if country != "Country Not Found":
        break

    return country


def _find_country_name(text):
    # Set default value
    country="Country Not Found"

    #Check if key exists in the text
    for key, value in cfg.Configuration.country_mapping.items():
       if key in text:
        country=value
        break
    
    return country