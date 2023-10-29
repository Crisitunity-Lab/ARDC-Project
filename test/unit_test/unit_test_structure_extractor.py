import unittest

import src.structure_extractor.data_utils as du
import src.structure_extractor.parsers as p

class TestStructureExtractor(unittest.TestCase):

    def test_year_calc(self):
        event = "2013_NY_train_crash"
        expected = "2013"
        actual = du._get_year_of_crisis(event)
        self.assertEqual(expected, actual)

    
    def test_country_mapping(self):
        event = "2013_NY_train_crash"
        expected = "US"
        actual = du._get_country_of_crisis(event)
        self.assertEqual(expected, actual)

    
    def test_event_mapping(self):
        event = "2013_NY_train_crash"
        expected = "Train Crash"
        actual = du._get_crisis_type(event)
        self.assertEqual(expected, actual)


    def test_message_length_1(self):
        message = "#korea #usa #news Deadly storms and floods in Sardinia: At least nine people are killed and a number are missi...  http://t.co/PQsiQsTEZX"
        expected = 17
        actual = du._get_message_length(message)
        self.assertEqual(expected, actual)


    def test_message_length_2(self):
        message = "RT @BBCBreaking: Photo shows #helicopter crash at #Clutha pub in Glasgow http://t.co/cYMa37HdjM &amp; http://t.co/gY03CIFj80"
        expected = 9
        actual = du._get_message_length(message)
        self.assertEqual(expected, actual)


    def test_country_name_1(self):
        text = "AU"
        expected = "Australia"
        actual = p._get_country_name(text)
        self.assertEqual(expected, actual)


    def test_country_name_2(self):
        text = "BRA"
        expected = "Brazil"
        actual = p._get_country_name(text)
        self.assertEqual(expected, actual)


    def test_country_name_3(self):
        text = "Republic of Malta"
        expected = "Malta"
        actual = p._get_country_name(text)
        self.assertEqual(expected, actual)

    
    def test_find_country_1(self):
        text = "The UK is a nice country, like España"
        expected = "United Kingdom"
        actual = p._find_country_name(text)
        self.assertEqual(expected, actual)


    def test_find_country_2(self):
        text = "Nutbush city limits"
        expected = "Country Not Found"
        actual = p._find_country_name(text)
        self.assertEqual(expected, actual)

    
    def test_parse_label_country_1(self):
        text = "This is Australia"
        expected = "Australia"
        actual = p.parse_label_country(text)
        self.assertEqual(expected, actual)


    def test_parse_label_country_2(self):
        text = "Paris, France"
        expected = "France"
        actual = p.parse_label_country(text)
        self.assertEqual(expected, actual)


    def test_parse_label_country_3(self):
        text = "DE"
        expected = "Germany"
        actual = p.parse_label_country(text)
        self.assertEqual(expected, actual)


    def test_parse_label_country_4(self):
        text = "Not a real country"
        expected = "Country Not Found"
        actual = p.parse_label_country(text)
        self.assertEqual(expected, actual)


    def test_clean_text(self):
        text = "#DollyTheSheep has a .fullstop"
        chars_to_remove = [".", "#"]
        expected = "DollyTheSheep has a fullstop"
        actual = p._clean_text(text, chars_to_remove)
        self.assertEqual(expected, actual)

    
    def test_get_position(self):
        text = "This is some text with a label"
        search_str = "label"
        expected = 25
        actual = p._get_position(text, search_str)
        self.assertEqual(expected, actual)

    
    def test_parse_label_infotype_1(self):
        text = 'Label: "Affected residents" there are people everywhere' 
        expected = "Affected individuals"
        actual = p.parse_label_infotype(text)
        self.assertEqual(expected, actual)


    def test_parse_label_infotype_2(self):
        text = 'Nothing to see here, move along' 
        expected = "Unknown"
        actual = p.parse_label_infotype(text)
        self.assertEqual(expected, actual)


    def test_parse_label_infotype_3(self):
        text = '"Affected residents"' 
        expected = "Affected individuals"
        actual = p.parse_label_infotype(text)
        self.assertEqual(expected, actual)


    def test_parse_label_infotype_4(self):
        text = 'Label: "Godzilla"' 
        expected = "Unknown"
        actual = p.parse_label_infotype(text)
        self.assertEqual(expected, actual)
    

    def test_parse_label_crisis_type_1(self):
        text =   '{"Crisis": "Bushfire"}'
        expected = "Wildfire"
        actual = p.parse_label_crisistype(text)
        self.assertEqual(expected, actual)
    

    def test_parse_label_crisis_type_2(self):
        text =   '''{"Crisis": "Flood" 
            Explanation: The text mentions "cleanup efforts" and "flood," 
            indicating that a flood-related crisis is underway.}'''
        expected = "Floods"
        actual = p.parse_label_crisistype(text)
        self.assertEqual(expected, actual)

    
    def test_parse_label_crisis_type_3(self):
        text =   'Crisis Nothing to find here'
        expected = "Unknown"
        actual = p.parse_label_crisistype(text)
        self.assertEqual(expected, actual)
    

    def test_singular_label(self):
        text = "Floods"
        expected = "Flood"
        actual = p._singular_label(text)
        self.assertEqual(expected, actual)