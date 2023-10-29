
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
    

    crisis_type_dict = dict({
    "Flood":"Floods",
    "Earthquake":"Earthquake",
    "Wildfire":"Wildfire",
    "Not labeled":"Not labeled",
    "Haze":"Haze",
    "Typhoon":"Typhoon",
    "Hurricane":"Typhoon",
    "Helicopter crash":"Crash",
    "Meteor":"Meteorite",
    "Fire":"Fire",
    "Derailment":"Derailment",
    "Boston marathon bombing":"Bombings",
    "Lax shooting":"Shootings",
    "Shooting":"Shootings",
    "Train derailment":"Derailment",
    "Train crash":"Derailment",
    "Flooding":"Floods",
    "Russian meteor":"Meteorite",
    "Glasgow helicopter crash":"Crash",
    "Boston bombing":"Bombings",
    "Unknown":"Unknown",
    "Explosion":"Explosion",
    "Fertilizer plant explosion":"Explosion",
    "Nyc train derailment":"Derailment",
    "Tsunami":"Tsunami",
    "Nightclub fire":"Fire",
    "Oil spill":"Oil spill",
    "Bangladesh factory collapse":"Collapse",
    "Bangladesh building collapse":"Collapse",
    "Building collapse":"Collapse",
    "Brazil nightclub fire":"Fire",
    "Boulder flood":"Floods",
    "Bombing":"Bombings",
    "Meteor shower":"Meteorite",
    "Meteorite":"Meteorite",
    "Train accident":"Derailment",
    "Terrorism":"Terrorism",
    "Cyclone":"Typhoon",
    "Oil train derailment":"Derailment",
    "Meteor strike":"Meteorite",
    "Texas explosion":"Explosion",
    "Ab flood":"Floods",
    "Texas fertilizer plant explosion":"Explosion",
    "Factory collapse":"Collapse",
    "Collapse":"Collapse",
    "Meteor explosion":"Meteorite",
    "Oil refinery explosion":"Explosion",
    "Qldflood":"Floods",
    "Metro-north derailment":"Derailment",
    "Boston marathon explosion":"Bombings",
    "Abflood":"Floods",
    "Coflood":"Floods",
    "Boulderflood":"Floods",
    "Tornado":"Tornado",
    "Colorado flood":"Floods",
    "Quake":"Earthquake",
    "West explosion":"Explosion",
    "Qld flood":"Floods",
    "Marathon bombing":"Bombings",
    "Fatal train crash":"Derailment",
    "Bangladesh flood":"Floods",
    "West texas explosion":"Explosion",
    "Quebec train derailment":"Derailment",
    "Police helicopter crash":"Crash",
    "Waco explosion":"Explosion",
    "Flash flooding":"Floods",
    "Quebec train crash":"Derailment",
    "Texas plant explosion":"Explosion",
    "Terrorist attack":"Terrorism",
    "Ny train crash":"Derailment",
    "Brazil fire":"Fire",
    "West, texas explosion":"Explosion",
    "Meteor blast":"Meteorite",
    "Bronx train derailment":"Derailment",
    "West texas fertilizer plant explosion":"Explosion",
    "Alberta flood":"Floods",
    "Kiss nightclub fire":"Fire",
    "Metro north train derailment":"Derailment",
    "Colorado flooding":"Floods",
    "Nyc derailment":"Derailment",
    "Train wreck":"Derailment",
    "New york train crash":"Derailment",
    "Forest fire":"Wildfire",
    "Garment factory collapse":"Collapse",
    "Clutha helicopter crash":"Crash",
    "Bangladesh garment factory collapse":"Collapse",
    "Dhaka factory collapse":"Collapse",
    "Airport shooting":"Shootings",
    "Plant explosion":"Explosion",
    "Dhaka building collapse":"Collapse",
    "Fertilizer plant blast":"Explosion",
    "Manila flood":"Floods",
    "Meteor impact":"Meteorite",
    "Tropical cyclone":"Typhoon",
    "Savar building collapse":"Collapse",
    "Sardinia flood":"Floods",
    "Brazil wildfire":"Wildfire",
    "Lax airport shooting":"Shootings",
    "Flash flood":"Floods",
    "Blast":"Explosion",
    "Bundaberg flood":"Floods",
    "Spain train crash":"Derailment",
    "West texas flood":"Floods",
    "Los angeles airport shooting":"Shootings",
    "Guatemala quake":"Earthquake",
    "Bush fire":"Wildfire"
})

    response_mapping = dict({
            'Wildfires': 'Wildfire',
            'Bushfires': 'Wildfire',
            'Bushfire': 'Wildfire',
            'Na': 'Not labeled',
            '[Na]': 'Not labeled',
            'Flood':'Floods',
            'Bombing': 'Bombings',
            'Shooting': 'Shootings',  
            "Not applicable": 'Not labeled',
            "Other useful information":'Other Useful Information',
            "Caution and advice for residents":'Caution and advice',
            "Affected resident": 'Affected individuals',
            "Infrastructure and utilities damage": 'Infrastructure and utilities',
            "Donations and volunteering": 'Donations and volunteering',
            "Donations or volunteering": 'Donations and volunteering',
            "Expressing sympathy and support for affected": 'Sympathy and support',
            "Warnings and advice for residents.": 'Caution and advice',
            'Philipinnes': 'Philippines',
            'Phillipines': 'Philippines',
            'UK': 'United Kingdom',
            'Venezuela': 'Venezuela, Bolivarian Republic of',
            'Russia': 'Russian Federation',
            'US': 'United States',
        })