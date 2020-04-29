import urllib2, math, sys, re, pyperclip
from bs4 import BeautifulSoup

final_output=""
xxx_template = """
[columns]
[url=http://flightrising.com/main.php?dragon=[ID]]
[img]http://flightrising.com/rendern/350/[ID_ROUNDED]/[ID]_350.png[/img]
[/url]

[nextcol]
[center]
[img]http://flightrising.com/images/icons/small_[GENDER].png[/img][img]http://flightrising.com/images/icons/[ELEMENT]_rune.png[/img]

-----
[center][b][COLOUR][/b][br]
[PRIMARY][br]
[SECONDARY][br]
[TERTIARY][br]
[EYES] Eyes[br]
-----
[emoji=[CURRENCY]]
  [COST][br][br]

[url=http://www1.flightrising.com/auction-house/buy/realm/dragons?d_id=[ID]&page=1&collapse=1][img]http://flightrising.com/images/layout/button_buyauction.png[/img][/url]
[/center][/columns]

------
""".replace("\n", "")


xxx_page = "http://www1.flightrising.com/lair/397434/845978"
page = urllib2.urlopen(xxx_page)
soup = BeautifulSoup(page, 'html.parser')

IDs = [str(ID_label.parent.parent.contents[1]).strip() for ID_label in soup.findAll(text="ID#:")]
rounded_IDs = [str(int(math.ceil((int(ID) + 1) / 100.0))) for ID in IDs]
genders = [gender.split()[1].lower() for gender in soup.findAll(text=re.compile("male$", re.I))]
elements = [str(ID_label.parent.parent.contents[1]).strip().split()[0].lower() for ID_label in soup.findAll(text="Eye Type:")]
colours = [str(ID_label.parent.parent.contents[1]).strip().split()[0] for ID_label in soup.findAll(text="Primary Gene:")]
primaries = [str(ID_label.parent.parent.contents[1]).strip().split()[1] for ID_label in soup.findAll(text="Primary Gene:")]
secondaries = [str(ID_label.parent.parent.contents[1]).strip().split()[1] for ID_label in soup.findAll(text="Secondary Gene:")]
tertiaries = [str(ID_label.parent.parent.contents[1]).strip().split()[1] for ID_label in soup.findAll(text="Tertiary Gene:")]
eyes = [str(ID_label.parent.parent.contents[1]).strip().split()[1] for ID_label in soup.findAll(text="Eye Type:")]

for i in range(len(IDs)): 
    dragon_page = urllib2.urlopen("http://www1.flightrising.com/main.php?dragon=" + IDs[i])
    soup = BeautifulSoup(dragon_page, 'html.parser')
    currency = soup.find("a", {"id": "buydrag"})['title'].split()
    cost = currency[-2]
    currency = currency[-1].lower()[:-1]

    out = xxx_template\
        .replace("[ID]", IDs[i])\
        .replace("[ID_ROUNDED]", rounded_IDs[i])\
        .replace("[GENDER]", genders[i])\
        .replace("[ELEMENT]", elements[i])\
        .replace("[COLOUR]", colours[i])\
        .replace("[PRIMARY]", primaries[i])\
        .replace("[SECONDARY]", secondaries[i])\
        .replace("[TERTIARY]", tertiaries[i])\
        .replace("[EYES]", eyes[i])\
        .replace("[COST]", cost)\
        .replace("[CURRENCY]", currency)

    final_output += out

near_template = """
[columns]
[url=http://flightrising.com/main.php?dragon=[ID]]
[img]http://flightrising.com/rendern/350/[ID_ROUNDED]/[ID]_350.png[/img]
[/url]

[nextcol]
[center]
[img]http://flightrising.com/images/icons/small_[GENDER].png[/img][img]http://flightrising.com/images/icons/[ELEMENT]_rune.png[/img]

-----
[center]
[PRIMARY][br]
[SECONDARY][br]
[TERTIARY][br]
[EYES] Eyes[br]
-----
[emoji=[CURRENCY]]
  [COST][br][br]

[url=http://www1.flightrising.com/auction-house/buy/realm/dragons?d_id=[ID]&page=1&collapse=1][img]http://flightrising.com/images/layout/button_buyauction.png[/img][/url]
[/center][/columns]

------
""".replace("\n", "")


near_page = "http://www1.flightrising.com/lair/397434/1426872"
page = urllib2.urlopen(near_page)
soup = BeautifulSoup(page, 'html.parser')

IDs = [str(ID_label.parent.parent.contents[1]).strip() for ID_label in soup.findAll(text="ID#:")]
rounded_IDs = [str(int(math.ceil((int(ID) + 1) / 100.0))) for ID in IDs]
genders = [gender.split()[1].lower() for gender in soup.findAll(text=re.compile("male$", re.I))]
elements = [str(ID_label.parent.parent.contents[1]).strip().split()[0].lower() for ID_label in soup.findAll(text="Eye Type:")]
colours = [str(ID_label.parent.parent.contents[1]).strip() for ID_label in soup.findAll(text="Primary Gene:")]
primaries = [str(ID_label.parent.parent.contents[1]).strip() for ID_label in soup.findAll(text="Primary Gene:")]
secondaries = [str(ID_label.parent.parent.contents[1]).strip() for ID_label in soup.findAll(text="Secondary Gene:")]
tertiaries = [str(ID_label.parent.parent.contents[1]).strip() for ID_label in soup.findAll(text="Tertiary Gene:")]
eyes = [str(ID_label.parent.parent.contents[1]).strip().split()[1] for ID_label in soup.findAll(text="Eye Type:")]

for i in range(len(IDs)): 
    dragon_page = urllib2.urlopen("http://www1.flightrising.com/main.php?dragon=" + IDs[i])
    soup = BeautifulSoup(dragon_page, 'html.parser')
    currency = soup.find("a", {"id": "buydrag"})['title'].split()
    cost = currency[-2]
    currency = currency[-1].lower()
    if (currency == "gems"): 
        currency = "gem"

    out = near_template\
        .replace("[ID]", IDs[i])\
        .replace("[ID_ROUNDED]", rounded_IDs[i])\
        .replace("[GENDER]", genders[i])\
        .replace("[ELEMENT]", elements[i])\
        .replace("[COLOUR]", colours[i])\
        .replace("[PRIMARY]", primaries[i])\
        .replace("[SECONDARY]", secondaries[i])\
        .replace("[TERTIARY]", tertiaries[i])\
        .replace("[EYES]", eyes[i])\
        .replace("[COST]", cost)\
        .replace("[CURRENCY]", currency)

    final_output += out



pyperclip.copy(final_output)


