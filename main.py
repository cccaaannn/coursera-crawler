import time
import requests
from bs4 import BeautifulSoup


def get_links(url):
    links = []
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")
    for link in s.findAll('a', {'class':'c-directory-link'}):
        test_2 = link.get('href')
        links.append("https://www.coursera.org" + test_2)
    return links


def get_lang(soup):
    content = soup.find_all("h4",attrs={"class":"H4_1k76nzj-o_O-weightBold_uvlhiv-o_O-bold_1byw3y2 m-b-0"})[-1]
    return content.contents[0].strip().replace("\n", " ")


def get_name(soup):
    content = soup.find("h1",attrs={"class":"H2_1pmnvep-o_O-weightNormal_s9jwp5-o_O-fontHeadline_1uu0gyz max-text-width-xl m-b-1s"})
    #content = s.find("h1",attrs={"data-reactid":"171"})
    return content.contents[0].strip().replace("\n", " ")


def get_info(soup):
    content = soup.find("div", attrs={"class": "content-inner"})
    return content.contents[0].strip().replace("\n", " ")                  #bu olmayınca taglarda geliyo fonksiyon kullanıncada özel karakterler gidiyo


def get_page_count(soup):
    content = soup.find_all("a",attrs={"class":"box number"})[-1]
    return content.contents[0].strip().replace("\n", " ")


def open_link(url):
    r = requests.get(url)
    return r


def parse_html(r):
    r.encoding = "utf-8"
    plain = r.text
    soup = BeautifulSoup(plain, "html.parser")
    return soup


def printlist(list):
    for i in range(len(list)):
        print(str(i) + " : " + list[i])



def write_content_to_file(content,file_name):

    with open("content\\" + file_name,'a', encoding='utf-8') as file:

        for i in range(len(content[0])):

            file.write("----------  " + str(i + 1) + "  ----------")
            file.write("\n")
            file.write("\n")
            file.write("-----LINK-----")
            file.write("\n")
            file.write("\n")
            file.write(content[0][i])
            file.write("\n")
            file.write("\n")
            file.write("-----LANG-----")
            file.write("\n")
            file.write("\n")
            file.write(content[1][i])
            file.write("\n")
            file.write("\n")
            file.write("-----TITLE-----")
            file.write("\n")
            file.write("\n")
            file.write(content[2][i])
            file.write("\n")
            file.write("\n")
            file.write("-----INFO-----")
            file.write("\n")
            file.write("\n")
            file.write(content[3][i])
            file.write("\n")
            file.write("\n")
            file.write("\n")
            file.write("\n")



def write_content_to_file_simple_form(content,file_name):
    with open("content\\" + file_name,'a', encoding='utf-8') as file:
        for i in range(len(content[0])):
            file.write(content[3][i])





#execution time
start = time.time()


r = open_link('https://www.coursera.org/directory/courses')
soup = parse_html(r)
page_count = int(get_page_count(soup))


links = []
for current_page in range(page_count):
    links += get_links('https://www.coursera.org/directory/courses?page=' + str(current_page))
    print("page number: " + (current_page + 1).__str__())

printlist(links)



#get information from collected links
content = [[],[],[],[]]
file_name_counter = 1
for i in range(len(links)):
    url = links[i].__str__()
    r = open_link(url)
    soup = parse_html(r)
    content[0].append(links[i])
    content[1].append(get_lang(soup))
    content[2].append(get_name(soup))
    content[3].append(get_info(soup))


    # write all courses to a seperate file one by one
    if content[1][0].__str__() == "English":
        file_name = "dict" + file_name_counter.__str__() + ".txt"
        write_content_to_file_simple_form(content, file_name)
        file_name_counter += 1
        print((i + 1).__str__() + "/" + len(links).__str__() + " : link done")
    content = [[], [], [], []]



print("execution time: " + (time.time() - start).__str__())

