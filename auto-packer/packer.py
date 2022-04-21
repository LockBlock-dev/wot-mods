from zipfile import ZipFile
from argparse import ArgumentParser
from py_compile import compile
import xml.etree.ElementTree as ET
import os

parser = ArgumentParser()
parser.add_argument("-u", "--username", required=True, help="dev username")
parser.add_argument("-n", "--name", default="mod", help="mod name")
parser.add_argument("-v", "--version", default="1.0.0", help="mod version")
parser.add_argument("-d", "--description", default="no description", help="mod description")
parser.add_argument("-f", "--folder", default="./res", help="res folder path")
args = parser.parse_args()

root = ET.Element("root")
ET.SubElement(root, "id").text = args.username + "." + args.name.replace(" ", "_")
ET.SubElement(root, "version").text = args.version
ET.SubElement(root, "name").text = args.name
ET.SubElement(root, "description").text = args.description

XML = ET.ElementTree(root)

res_folder = os.path.normpath(os.path.join(os.getcwd(), args.folder))

if not os.path.isdir(res_folder):
    raise ValueError("Incorrect path to a res folder!")

if not os.path.exists("./build"):
    os.mkdir("./build")

files = os.listdir("./build")

for i in range(len(files)):
    os.remove("./build/" + files[i])

XML.write("./build/meta.xml")

def addFolder(file, folder): 
    for elem in os.listdir(folder):
        full_path = os.path.join(folder, elem)
        if os.path.isfile(full_path):
            if os.path.splitext(full_path)[1] == ".py":
                compile(full_path)
                file.write(full_path + "c", "./res" + full_path.split("res", 1)[1] + "c")
                os.remove(full_path + "c")
            else:
                file.write(full_path, "./res" + full_path.split("res", 1)[1])
        elif os.path.isdir(full_path):
            addFolder(file, full_path)

package = ZipFile("./build/" + args.username + "." + args.name.replace(" ", "_") + "_" + args.version + ".wotmod", "w")
package.write("./build/meta.xml", "meta.xml")
addFolder(package, res_folder)

os.remove("./build/meta.xml")
