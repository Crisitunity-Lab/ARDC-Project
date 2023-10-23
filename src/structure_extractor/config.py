
class Configuration:
    countries = dict({
        '2012_Colorado_wildfires':'US',
        '2013_Colorado_floods':'US',
        '2013_Glasgow_helicopter_crash':'GB',
        '2013_Brazil_nightclub_fire':'BR',
        '2013_Russia_meteor':'RU',
        '2013_Sardinia_floods':"IT",
        '2012_Philipinnes_floods':'PH',
        '2012_Costa_Rica_earthquake':'CR',
        '2012_Venezuela_refinery':'VE',
        '2013_Alberta_floods':'CA',
        '2013_Queensland_floods':'AU',
        '2013_NY_train_crash':'US',
        '2013_Australia_bushfire':'AU',
        '2013_LA_airport_shootings':'US',
        '2012_Typhoon_Pablo':'PH',
        '2013_Lac_Megantic_train_crash':'CA',
        '2013_Spain_train_crash':'ES',
        '2013_West_Texas_explosion':'US',
        '2012_Guatemala_earthquake':'GT',
        '2013_Savar_building_collapse':'BD',
        '2012_Italy_earthquakes':'IT',
        '2013_Bohol_earthquake':'PH',
        '2013_Singapore_haze':'SG',
        '2013_Boston_bombings':'US',
        '2013_Manila_floods':'PH',
        '2013_Typhoon_Yolanda':'PH'
    })

    crisis_type = dict({
        '2012_Colorado_wildfires':'Wildfire',
        '2013_Colorado_floods':'Flood',
        '2013_Glasgow_helicopter_crash':'Helicopter Crash',
        '2013_Brazil_nightclub_fire':'Nightclub Fire',
        '2013_Russia_meteor':'Meteor',
        '2013_Sardinia_floods':"Flood",
        '2012_Philipinnes_floods':'Flood',
        '2012_Costa_Rica_earthquake':'Earthquake',
        '2012_Venezuela_refinery':'Explosion',
        '2013_Alberta_floods':'Flood',
        '2013_Queensland_floods':'Flood',
        '2013_NY_train_crash':'Train Crash',
        '2013_Australia_bushfire':'Bushfire',
        '2013_LA_airport_shootings':'Terrorism',
        '2012_Typhoon_Pablo':'Typhoon',
        '2013_Lac_Megantic_train_crash':'Train Crash',
        '2013_Spain_train_crash':'Train Crash',
        '2013_West_Texas_explosion':'Explosion',
        '2012_Guatemala_earthquake':'Earthquake',
        '2013_Savar_building_collapse':'Building Collapse',
        '2012_Italy_earthquakes':'Earthquake',
        '2013_Bohol_earthquake':'Earthquake',
        '2013_Singapore_haze':'Haze',
        '2013_Boston_bombings':'Terrorism',
        '2013_Manila_floods':'Flood',
        '2013_Typhoon_Yolanda':'Typhoon'
    })


    country_mapping = dict({
        'UK':"United Kingdom",
        'Syria':"Syrian Arab Republic",
        'Russia':"Russian Federation",
        'Scotland':"United Kingdom",
        'Venezuela':"Venezuela, Bolivarian Republic of",
        'VZL':"Venezuela, Bolivarian Republic of",
        'VZ':"Venezuela, Bolivarian Republic of" ,
        'SP':"Spain",
         'España':"Spain"
    })

    informativeness_labels = [
        "Related but not informative",
        "Related and informative",
        "Not related"
        ]
    
    information_type_labels =  [
        "Caution and advice for residents",
        "Affected residents",
        "Infrastructure and utilities damage",
        "Donations or volunteering",
        "expressing Sympathy and support for affected",
        "other useful information",
        "Not applicable"
        ]