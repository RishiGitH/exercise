from xml.etree import ElementTree as ET
import copy

class XmlParser:
    def __init__(self, xml_file):
        self.xml_file=xml_file

    def parse_xml_file(self):
        return ET.parse(self.xml_file)

    def get_root_node(self, xml_tree):
        return xml_tree.getroot()

    def recursively_create_dict_from_tree(self, curr_node):

        child_nodes_list=[]
        for child in curr_node:
            if len(child) > 0:
                child_dict = copy.deepcopy(self.recursively_create_dict_from_tree(child))
                child_nodes_list.append(child_dict)
            else:
                child_nodes_list.append({child.tag: child.text})
        if not child_nodes_list:
            output={curr_node.tag : ""}
        else:
            output={curr_node.tag: child_nodes_list}

        return output


    def convert_xml_file_into_dictionary(self):
        xml_tree = self.parse_xml_file()
        root_node= self.get_root_node(xml_tree)

        return self.recursively_create_dict_from_tree(root_node)






