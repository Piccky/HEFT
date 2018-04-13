import xml.etree.ElementTree as ET

tree = ET.ElementTree(file='doc1.xml')
root=tree.getroot()
root.tag, root.attrib
for child_of_root in root:
    print (child_of_root.tag, child_of_root.attrib)
print(root[0].tag, root[0].text)