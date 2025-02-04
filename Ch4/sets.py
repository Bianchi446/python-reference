# Script: Find the dial codes that contain a '1' in them in the dial_codes list 


dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
    (48, 'Poland'),
    (351, 'Portugal'),
    (974, 'Qatar'),
    (40, 'Romania'),
    (7, 'Russia'),
    (966, 'Saudi Arabia'),
    (65, 'Singapore'),
    (421, 'Slovakia'),
    (386, 'Slovenia'),
    (27, 'South Africa'),
    (34, 'Spain'),
    (94, 'Sri Lanka'),
    (46, 'Sweden'),
    (41, 'Switzerland'),
    (886, 'Taiwan'),
    (66, 'Thailand'),
    (90, 'Turkey'),
    (971, 'United Arab Emirates'),
    (44, 'United Kingdom'),
    (1, 'United States'),
    (598, 'Uruguay'),
    (58, 'Venezuela'),
    (84, 'Vietnam'),
    (260, 'Zambia'),
    (263, 'Zimbabwe'),
]

# The haystack (all dial codes)
haystack = [code for code, country in dial_codes]

# The needles (dial codes containing the digit 1)
needles = [code for code in haystack if '1' in str(code)]

print("Dial codes containing the digit 1:", needles)
