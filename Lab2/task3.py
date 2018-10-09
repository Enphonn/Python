import collections
import xml.etree.ElementTree as et

def find_equal(file):
    words = list((open(file).read().lower()).split())
    return collections.Counter(words)

voc = find_equal("file.txt")


root = et.Element("root")
doc = et.SubElement(root, "doc")
p =0
for key  in  voc:
    et.SubElement(doc,"field"+str(p),name = key).text = str(voc[key])

    p+=1
tree = et.ElementTree(root)
tree.write("list.xml")
