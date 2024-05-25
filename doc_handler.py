import json

def list_page_soup(output): #to check all the parse
    f = open("list_page_soup.txt", "wb")
    f.write(output.encode('utf-8'))
    f.close()

def detail_page_soup(output): #to check all the parse
    f = open("detail_page_soup.txt", "wb")
    f.write(output.encode('utf-8'))
    f.close()

def listing(output):
    f = open("lis.txt", "a")
    f.write(output)
    f.write("\n")
    f.close()


def Doc_handler(dict_item):
    f = open("item_attr.txt", "a")
    json_objct=json.dumps(dict_item)
    f.write(json_objct)
    f.write("\n")
    f.close()

def Doc_handler_BigDescription(dict_item):
    f = open("BigDescription.txt", "a")
    json_objct=json.dumps(dict_item)
    f.write(json_objct)
    f.write("\n")
    f.close()

def Doc_handler_Supplier(dict_item):
    f = open("Supplier.txt", "a")
    json_objct=json.dumps(dict_item)
    f.write(json_objct)
    f.write("\n")
    f.close()

def all_soup(output):
    f = open("debugging.txt", "a", encoding="utf-8")
    #with open(output, "w", encoding="utf-8") as f:
    f.write(output)
    f.close()