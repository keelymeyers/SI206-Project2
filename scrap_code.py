UMSI = "https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastna me_value=&rid=All"
    #count = 11
    #while count != 0:
    #UMSI = base_url + "&page=" + str(count)
    #count = count -1
    UMSI_html = requests.get(UMSI, headers={'User-Agent': 'SI_CLASS'})
    x = UMSI_html.text
    umsi_soup = BeautifulSoup(x, 'html.parser')
    tags = umsi_soup.find_all("div", "field-item even", "dc:title")
    for t in tags:
        print (t)
    #umsi_titles[tags] = tags.text
    print (umsi_titles)
    #print (umsi_soup)
    #Your code here



#working as of 10:00 PM

UMSI_html = requests.get(UMSI, headers={'User-Agent': 'SI_CLASS'})
    x = UMSI_html.text
    umsi_soup = BeautifulSoup(x, 'html.parser')
    name_tags = umsi_soup.find_all("div", class_="field-item even", property="dc:title")
    for t in name_tags:
        name = t.find_all('h2')
        for n in name:
            print (n.text)


        title = t.find_all("div", class_="field field-name-field-person-titles field-type-text field-label-hidden")
        print (title)
        
        for t in title:
            print (t.text)
            umsi_titles[n.text] = t.text
            print (umsi_titles[n.text])
    print (umsi_titles)
        

#working as of 10:24 for first page of UMSI directory
