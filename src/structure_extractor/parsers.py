import inflect
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
  chars_to_remove = ["-","."]
  text_loc = _get_position(text, search_text)
  start_pos = text_loc + len(search_text)

  if text_loc != -1:
    second_loc = text.find(":", start_pos)
    if second_loc != -1:
      substring = text[start_pos:second_loc]
      
      for label in cfg.Configuration.informativeness_labels:
        if label.lower() in substring.lower():
          label = _clean_text(label, chars_to_remove)
          return label
      
  for label in cfg.Configuration.informativeness_labels:
    if label.lower() in text.lower():
      label = _clean_text(label, chars_to_remove)
      return label

  value = re.findall(r'"(.*?)"', text)
  if value:
    label = value[0]
    label = _clean_text(label, chars_to_remove)
    return label
  
  return "Unknown"


def parse_label_infotype(text):
    
    # Remove period and hashtags from text
    chars_to_remove = [".", "#"]
    text = _clean_text(text, chars_to_remove)

    substring = None
    output = None
    search_text = "label:"
    text_lower = text.lower()
    search_text_len = len(search_text)
    value = re.findall(r'"(.*?)"', text)

    # Get position of "label:" in response (if it exists)
    text_loc = _get_position(text_lower, search_text)
    start_pos = text_loc + search_text_len

    if text_loc != -1:
        second_loc = text.find(":", start_pos)
        if second_loc != -1:
            substring = text[start_pos:second_loc]
            for label in cfg.Configuration.information_type_labels:
                if label.lower() in substring.lower():
                    output = label
                    break
    
    # If substring not found in config then try finding a label in the whole text
    if not(output):
      for label in cfg.Configuration.information_type_labels:
          if label.lower() in text_lower:
              output = label
              break
    
    if not(output) and value:
        output = value[0]
    
    output = output or substring

    # Set default for label
    output = output or "Unknown"

    # Remove plurals
    output = _singular_label(output)

     # Map response type to standard crisis type labels (e.g. Bushfire to Wildfire)
    output = response_mapping(output)

    return output


def parse_label_crisistype(text):

  substring = None
  search_text = '"crisis": '
  text_lower = text.lower()
  search_text_len = len(search_text)

  # Get position of "label:" in response (if it exists)
  text_loc = _get_position(text_lower, search_text)
  start_pos = text_loc + search_text_len

  if text_loc != -1:

    # Get text after crisis label
    substring = text[start_pos:]

    # Find the index of the closing double quote or closing quote
    if substring.startswith('"'):
      end_index = substring.find('"',1)

      # If there is a second double quote get text between double quotes
      if end_index != -1:
        output = substring[1:end_index]
      else:
        output = "missing 2nd apostrophe"
    else:
      end_index = substring.find("\n")
      if end_index != -1:
        output = substring[:end_index]
      else:
        output = "missing '\n'"
  else:
    output = "Unknown"
  
  # If the output label is a plural change to singular (i.e. Floods = Flood).
  # This is for standardising responses
  prelim = _singular_label(output)

  # Map response type to standard crisis type labels (e.g. Bushfire to Wildfire)
  label = response_mapping(prelim)
  
  return label
  

def response_mapping(text):
    # Set default value
    response = "Unknown"

    #Check if key exists in the text
    for key, value in cfg.Configuration.response_mapping.items():
       if key in text:
        response = value
        break
    
    return response


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


def _clean_text(text, chars_to_remove=[".", "#"]):
  pattern="[" + "".join(chars_to_remove) + "]"
  result=re.sub(pattern, '', text)
  return result


def _get_position(text, search_str):
   pos=text.find(search_str)
   return pos


def _singular_label(text):
    
    # Create an instance of the inflect engine
    p = inflect.engine()
    
    # Convert a plural word to a singular word
    output = p.singular_noun(text) or text

    # Change sentence case
    output = output.capitalize()

    return output
