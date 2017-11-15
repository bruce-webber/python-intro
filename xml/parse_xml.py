"""
This is a demonstration of xml.etree (part of the standard library), which is used
to parse, modify and create XML files.
"""

import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()

# The top level tag.
print(root.tag)

# The tag of the first sub-element.
print(root[0].tag)

# The attributes of the first sub-element.
print(root[0].attrib)
print()

# The names of the countries and their neighbors.
for country in root:
    if 'name' in country.attrib:
        print(country.attrib['name'])
        for element in country:
            if element.tag == 'neighbor':
                if 'name' in element.attrib:
                    print('    ' + element.attrib['name'])
