import pycountry
import re

import src.structure_extractor.config as cfg


def parse_label_country(text):
    # Remove the word "ISO" from the string
    text = text.replace("ISO", "")

    country = _get_country_name(text)

    if country == "Country Not Found":
       country = _find_country_name(text)
        
    return country


def parse_label_informativenss(text):

  search_text = "Label:"
  chars_to_remove = ["- "]
  text_loc = _get_position(text, search_text)
  start_pos = text_loc + len(search_text)

  if text_loc != -1:
    second_loc = text.find(":", start_pos)
    if second_loc != -1:
      substring = text[start_pos:second_loc]
      
      for label in cfg.Configuration.informativeness_labels:
        if label.lower() in substring.lower():
          label = _clean_info_type_text(label, chars_to_remove)
          return label
      
  for label in cfg.Configuration.informativeness_labels:
    if label.lower() in text.lower():
      label = _clean_info_type_text(label, chars_to_remove)
      return label

  value = re.findall(r'"(.*?)"', text)
  if value:
    label = value[0]
    label = _clean_info_type_text(label, chars_to_remove)
    return label
  
  return "Unknown"


def parse_label_infotype(text):
    
    # Remove period and hashtags from text
    chars_to_remove = [".", "#"]
    text = _clean_info_type_text(text, chars_to_remove)

    substring = None
    search_text = "label:"
    text_lower = text.lower()
    search_text_len = len(search_text)

    # Get position of "label:" in response (if it exists)
    text_loc = _get_position(text_lower, search_text)
    start_pos = text_loc + search_text_len

    if text_loc != -1:
        second_loc = text.find(":", start_pos)
        if second_loc != -1:
            substring = text[start_pos:second_loc]
            for label in cfg.Configuration.information_type_labels:
                if label.lower() in substring.lower():
                    return label 
    
    for label in cfg.Configuration.information_type_labels:
        if label.lower() in text_lower:
            return label

    value = re.findall(r'"(.*?)"', text)
    
    if value:
        return value[0]
    if substring:
       return substring

    return "Unknown"


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


def _clean_info_type_text(text, chars_to_remove=[".", "#"]):
  pattern="[" + "".join(chars_to_remove) + "]"
  result=re.sub(pattern, '', text)
  return result


def _get_position(text, search_str):
   pos=text.find(search_str)
   return pos