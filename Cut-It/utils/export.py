"""
    - Logic to export a card (in HTML form) to various filetypes (docx, pdf)
    - TODO: add docx support
"""

import json
import re
import time

import chromedriver_autoinstaller
from selenium import webdriver


def printPDF(body, path, cardName = "Cut-It Export"):
    """Saves html to pdf with Selenium

    Args:
        body (str): the "body" section of the html
        path (str): path to the save folder
        cardName (str, optional): the name of the card (becomes filename). Defaults to "Cut-It Export".
    """

    # Pagifying card body w/ appropriate title
    html = f"<!DOCTYPE html><html><head><title>{cardName}</title></head>{body}</html>"
    html = re.escape(html)

    # generating version-appropriate driver
    chromedriver_autoinstaller.install()

    # Adding print config, app mode, log level, window size
    chrome_options = webdriver.ChromeOptions()

    settings = {
        "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": ""
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2,
        "isHeaderFooterEnabled": False,
        "mediaSize": {
            "height_microns": 279400,
            "name": "ANSI_A",
            "width_microns": 215900,
            "custom_display_name": "ANSI_A"
        },
        "customMargins": {},
        "marginsType": 2,
        # "scaling": 175,
        # "scalingType": 3,
        # "scalingTypePdf": 3,
        "isCssBackgroundEnabled": True
    }

    prefs = {
        'printing.print_preview_sticky_settings.appState': json.dumps(settings),
        'savefile.default_directory': path
    }

    chrome_options.add_argument('--enable-print-browser')
    chrome_options.add_argument('--kiosk-printing')
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument("--log-level=3")

    chrome_options.add_argument("--app=http://cutit.cards")

    chrome_options.add_argument("--window-size=600,400")

    # Creating browser
    browser = webdriver.Chrome(options=chrome_options)

    # Overwriting HTML
    browser.execute_script(f"document.write(`{html}`)")

    # Waiting for load and saving
    time.sleep(2)
    browser.execute_script('window.print()')
    time.sleep(1.5)
    browser.close()

if __name__ == "__main__":
    t = """
        <!DOCTYPE html><html><head><title>Cut-It Export</title></head><body style="font-family: Times New Roman"><p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:bold; text-decoration: underline; background-color:#00ffff;">Levenson '21<br/></span>CNN • https://www.cnn.com/2021/07/07/us/miami-dade-building-collapse-wednesday/index.html<br/>Levenson, Madeline. "10 more bodies found in Surfside condo collapse rubble, pushing death toll to 46" CNN, 07/07/2021, https://www.cnn.com/2021/07/07/us/miami-dade-building-collapse-wednesday/index.html. Accessed 7/7/2021.<br/><br/>10 more bodies found in Surfside condo collapse rubble, pushing death toll to 46By Madeline Holcombe and Eric Levenson, CNNUpdated 4:18 PM ET, Wed July 7, 2021 JUST WATCHEDVideo shows demolition of remainder of Surfside buildingReplayMore Videos ...MUST WATCH (18 Videos)Video shows demolition of remainder of Surfside buildingStructural engineer explains damage shown in condo photosDeSantis speaks from Surfside: Community outpouring has been moving Biden opens up about grief at Surfside collapse visitMan avoids condo collapse after girlfriend requests he stay with herShe sued condo in 2015. Why her attorney remained worriedTeen says saving elderly woman was 'a blessing in disguise'Hear daughter's heartbreaking answer when asked if she wants to meet with BidenCondo owners were facing $15M in assessments for building repairsFamily says they found grandmother's photos, birthday card in debrisCouple explains why they aren't leaving sister tower of collapsed condo'It's not enough!': Frustrated mom lashes out at Florida officials Children of missing woman say dad was out of town when condo collapsedStructural engineer discusses concerns raised in 2018 reportEngineer raised concerns about structural damage at Surfside condominium in 2018 reportHear story of woman missing 7 family members in condo collapse$5M lawsuit filed against association of collapsed Florida building'Have hope': Hear fire chief's emotional message to families (CNN)Ten more bodies were found in the rubble of a condo collapse in Surfside, Florida, pushing the confirmed death toll to 46 -- with another 94 people still unaccounted for, Miami-Dade Mayor Daniella Levine Cava said Wednesday."As the magnitude of this catastrophe continues to grow each and every day since the collapse, our community and the
    world are grieving with all of the families who are living through this unthinkable tragedy," she said.Search and rescue efforts to find survivors amid the rubble of the building have become increasingly grim. Miami-Dade Fire Chief Alan Cominsky said Wednesday that search and rescue personnel combing the rubble have found no evidence that anyone survived the initial collapse.A day earlier, he said there had been no signs of any voids or livable spaces amid the wreckage where people might have survived."We're definitely searching," he said. "We're not coming across that."Read MoreOn Wednesday afternoon, a group
    of collapse survivors gathered at a local hotel to receive a multiple police vehicle escort back to the collapse site. The cluster of survivors gathered in the lobby of the hotel, being advised by uniformed police offers, officers in plain clothes, red cross workers and what appeared to be grief counselors.A woman in her sixties said she was heading back to the Champlain South collapse site. "I'm just sad, but I want to see it," she told CNN.The search continued Wednesday through inclement weather from Tropical Storm Elsa, which passed by the opposite coast of Florida. Winds of up to 30 miles per hour walloped
    crews Tuesday, but the weather had largely cleared by midday Wednesday, Cava said.Rescue crews battle storms as they search for dozens still unaccounted for in Florida condo collapseThe condo's collapse has raised questions about whether other residential structures could be at risk in Miami-Dade County, where sea levels are rising, the salty air is corrosive and nearly two-thirds of all commercial, condo and apartment buildings are as old or older than the 40-year-old building that collapsed, according to a CNN analysis of county records.Florida's legal community has created a safety task force to review laws
    governing the state's condominium development industry in the wake of the catastrophic collapse of a condo building in Miami-Dade County two weeks ago, according to a statement Tuesday.The Condominium Law and Policy on Life Safety Task Force is intended to serve residents of the state and was created by the
    Real Property, Probate, and Trust Law Section of the Florida Bar, according to the statement."The Task Force will serve as a resource to the Governor and Legislature as they review all aspects of Florida condominium law, development, association operations, and maintenance to determine and recommend if legislative and or regulatory changes should be enacted to minimize the likelihood of a similar tragedy," Bob Swain, chairperson of the Florida Bar Real Property, Probate, and Trust Law Section, said in a statement.How to help Surfside VictimsTeams not finding anything positive, but still more space to search Photos: Deadly condo collapse near MiamiRescue crews work at the site of the collapsed building in Surfside, Florida, on Tuesday, July 6. Hide Caption 1 of 53 Photos: Deadly condo collapse near MiamiMembers of a search-and-rescue team comb through the debris on Monday.Hide Caption 2 of 53 Photos: Deadly condo collapse near MiamiA memorial is seen near the spot where the building used to be. The rest of the building was demolished Sunday so that authorities could continue to look for survivors safely, officials said.Hide Caption 3 of 53 Photos: Deadly condo collapse near MiamiA controlled explosion brings down the
    unstable remains of the building on Sunday.Hide Caption 4 of 53 Photos: Deadly condo collapse near MiamiA woman cries as she watches the rest of Champlain Towers South be demolished.Hide Caption 5 of 53 Photos: Deadly condo collapse near MiamiPeople watch a cloud of dust form as the rest of the building is demolished.Hide Caption 6 of 53 Photos: Deadly condo collapse near MiamiKarol Casper places a flower on the memorial wall set up near the building on Sunday.Hide Caption 7 of 53 Photos: Deadly condo collapse near MiamiPeople stop at a makeshift memorial near the site.Hide Caption 8 of 53 Photos: Deadly condo
    collapse near MiamiSearch-and-rescue personnel work at the site on Friday.Hide Caption 9 of 53 Photos: Deadly condo collapse near MiamiResidents of the Crestview Towers Condominium carry their belongings as they leave their building in North Miami Beach, Florida, on Friday. The building, about 6 miles from Surfside, was deemed to be structurally and electrically unsafe based on a delinquent recertification report for the almost 50-year-old building. The city said the move was out of an "abundance of caution," as area authorities check high-rise condo buildings following the Surfside collapse.Hide Caption 10 of
    53 Photos: Deadly condo collapse near MiamiPresident Joe Biden and first lady Jill Biden visit a memorial near the partially collapsed building on Thursday. Biden traveled to Surfside to console families still waiting on news of their loved ones. Those meetings were closed to the press.Hide Caption 11 of 53
    Photos: Deadly condo collapse near MiamiA Coast Guard boat patrols the water ahead of Biden's visit on Thursday.Hide Caption 12 of 53 Photos: Deadly condo collapse near MiamiNBA basketball player Udonis Haslem, left, and Miami-Dade County Mayor Daniella Levine Cava arrive to pay their respects at a memorial
    near the building on June 30.Hide Caption 13 of 53 Photos: Deadly condo collapse near MiamiSearch-and-rescue teams look through the rubble of Champlain Towers South on June 29.Hide Caption 14 of 53 Photos: Deadly condo collapse near MiamiPeople take part in a twilight vigil near the building on June 28.Hide
    Caption 15 of 53 Photos: Deadly condo collapse near MiamiMembers of the Legendarios, a men's religious group, gather near the building for a moment of prayer.Hide Caption 16 of 53 Photos: Deadly condo collapse near MiamiMore than 3 million pounds of concrete have already been removed during the rescue operation, said Miami-Dade Fire Chief Alan Cominsky.Hide Caption 17 of 53 Photos: Deadly condo collapse near MiamiA woman puts flowers in a barricade as she pays her respects near the building.Hide Caption 18 of 53 Photos: Deadly condo collapse near MiamiPassersby look at photos of missing people.Hide Caption 19 of 53 Photos: Deadly condo collapse near MiamiWorkers search through the rubble on June 26.Hide Caption 20 of 53 Photos: Deadly condo collapse near MiamiEliagne Sanchez and K. Parker lay flowers on the beach near the partially collapsed building.Hide Caption 21 of 53 Photos: Deadly condo collapse near MiamiSmoke rises as rescuers continued to search for survivors on June 26.Hide Caption 22 of 53 Photos: Deadly condo collapse near MiamiPeople stand near the building on June 25.Hide Caption 23 of 53 Photos: Deadly condo collapse near MiamiMourners light candles on the beach near the building.Hide Caption 24 of 53
    Photos: Deadly condo collapse near MiamiMembers of a search-and-rescue team work in the rubble.Hide Caption 25 of 53 Photos: Deadly condo collapse near MiamiPeople pray together on the beach near the collapsed building.Hide Caption 26 of 53 Photos: Deadly condo collapse near MiamiFirefighters battle a blaze
    at the collapse site.Hide Caption 27 of 53 Photos: Deadly condo collapse near MiamiPeople hug June 25 as they wait for news about their relatives at a community center in Surfside.Hide Caption 28 of 53 Photos: Deadly condo collapse near MiamiRescue personnel search through the building's rubble on June 25.Hide Caption 29 of 53 Photos: Deadly condo collapse near MiamiToby Fried holds up a picture of her missing brother, Chaim Rosenberg, outside the Surfside Community Center on June 25.Hide Caption 30 of 53 Photos: Deadly condo collapse near MiamiRescue workers use a crane to inspect the damage.Hide Caption 31 of 53 Photos: Deadly condo collapse near MiamiAriana Hevia, center, stands with Sean Wilt near the partially collapsed building on June 25. Hevia's mother, Cassandra Statton, lives in the building.Hide Caption 32 of 53 Photos: Deadly condo collapse near MiamiRescue workers arrive to the scene with dogs on June 25.Hide Caption 33 of 53 Photos: Deadly condo collapse near MiamiFaydah Bushnaq, center, is hugged by Maria Fernanda Martinez as they stand on the beach near the building. Bushnaq, who was vacationing in South Florida, stopped to write "pray for their souls" in the sand.Hide Caption 34 of 53 Photos: Deadly
    condo collapse near MiamiThe arm of an earth mover is seen during the search operations.Hide Caption 35 of 53 Photos: Deadly condo collapse near MiamiRescue personnel work at the site on June 24.Hide Caption 36 of 53 Photos: Deadly condo collapse near MiamiYube Pettingill talks to the media. Two of her family members were still missing.Hide Caption 37 of 53 Photos: Deadly condo collapse near MiamiThis photo was tweeted by Miami-Dade Fire Rescue after the building collapsed.Hide Caption 38 of 53 Photos: Deadly condo collapse near MiamiDisplaced residents are taken to a nearby hotel in Surfside.Hide Caption 39 of 53 Photos: Deadly condo collapse near MiamiThe partial collapse left huge piles of rubble and materials dangling from what remained of the structure.Hide Caption 40 of 53 Photos: Deadly condo collapse near MiamiFlorida Gov. Ron DeSantis, at center in the red tie, arrives to speak to the media on June 24. "We still have hope to be able to identify additional survivors," DeSantis told reporters near the scene. "The state of Florida, we're offering any assistance that we can."Hide Caption 41 of 53 Photos: Deadly condo collapse near MiamiDebris dangles from the building on June 24.Hide Caption 42 of 53 Photos: Deadly condo collapse near MiamiPeople hug at a family reunification center where evacuees were staying in Surfside.Hide Caption 43 of 53 Photos: Deadly condo collapse near MiamiThe cause of the collapse wasn't immediately known.Hide Caption 44 of 53 Photos: Deadly condo collapse near MiamiJennifer Carr sits with her daughter as they and other evacuees wait for news at the family reunification center in Surfside.Hide Caption 45 of 53 Photos: Deadly condo collapse near MiamiRescue personnel search through the rubble with dogs.Hide Caption 46 of 53 Photos: Deadly condo collapse near MiamiPolice stand guard on the day the building collapsed.Hide Caption 47 of 53 Photos: Deadly condo collapse near MiamiPeople on the beach look at the building after the partial collapse.Hide Caption 48 of 53 Photos: Deadly condo collapse near MiamiThe building was constructed in 1981, according to online Miami-Dade property records.Hide Caption 49 of 53 Photos: Deadly condo collapse near MiamiPeople lie on cots at the family reunification center in Surfside.Hide Caption 50 of 53 Photos: Deadly condo collapse near MiamiThe beachfront community is a few miles north of Miami Beach.Hide Caption 51 of 53 Photos: Deadly condo collapse near MiamiMore than 80 rescue units responded to the scene, Miami-Dade Fire Rescue said.Hide Caption 52 of 53 Photos: Deadly condo collapse near MiamiRescue personnel work at the site of the partial collapse.Hide Caption 53 of 53Officials have said that despite the time that has passed, they remain hopeful they will still find survivors. The key to finding survivors, Cominsky said, is finding voids or livable spaces among the rubble.About 5 million pounds of debris have been removed from the site so far, Cominsky said. But with the amount of ground to cover, there is no telling what the teams will find in the coming days,
    Cominsky said.The site has been broken up into grids, none of which have been fully cleared yet. The way the building collapsed as well as the magnitude of it means that teams have been able to get further down on some areas than others so far, he said.A college student, the daughter of a Miami firefighter,
    a family of four: What we know about the collapse victimsTeams continue to search "as aggressive as we can to see if we can assist with the families and locate individuals," he said. Tuesday was a day of gratitude for one family, when the uncle of a 15-year-old called the man who pulled the boy from the rubble just after the collapse to thank him.Nicholas Balboa told CNN on Tuesday that he heard 15-year-old Jonah Handler screaming under the rubble after the condo building collapsed. Balboa was not in the building but was standing nearby when it collapsed. Balboa said Jonah's uncle told him Jonah was out of the
    hospital with only minor injuries. Since the collapse, Balboa says he has replayed that moment in his mind many times, wondering what he could have done differently to save more people, he said. Four additional bodies were recovered Tuesday, Levine Cava said. The victims of the collapse range in age from 4 to 92.With rescue efforts still underway, some families have asked to visit the collapse site, Surfside Mayor Charles Burkett said."Of course, we have to work around the rescue efforts," he said. "I think it would be very, very good for those families to again see the amazing efforts that are being expended on their behalf." Debris held for investigationSearch and rescue teams continue to work in the rubble at the site of the collapsed Champlain Towers South condo in Surfside.Meanwhile, more federal organizations are investigating why the building collapsed. Mayor Levine Cava said the National Institute of Standards and Technology (NIST), the US Geological Survey and the National Science Foundation are sending staff."NIST, our federal partner, continues to work closely with the structural specialists, with detectives, and the fire rescue crews on site, as the evidence gathering process is well underway," she said."They're capturing all possible insights from the debris and all evidence is being properly tagged and logged."'Tragedy beyond tragedy': Champlain Towers South was a catastrophe in slow motion All of the debris removed from the site is considered "evidentiary debris," Levine Cava said. The remnants are being
    sorted on-site, and any objects that can be distinguished are put in certain bins and labeled as to their exact location, the mayor said.The county has created a form for family members to document their belongings, which will be an active part of the investigation, Levine Cava said."The families are not reviewing what's come out of the site at this time, but we have photographs, they have their information, and as we move forward, we'll be attempting to do matching and releasing it to them as soon as we can, given the active investigation," she said.CNN's Rosa Flores, John Couwels, Amanda Watts, Rebekah Riess, Leyla Santiago, Gregory Lemos, David Shortell, Curt Devine and Paul Vercammen contributed to this report.JUST WATCHEDVideo shows demolition of remainder of Surfside buildingReplayMore Videos ...MUST WATCH (18 Videos)Video shows demolition of remainder of Surfside buildingStructural engineer explains damage
    shown in condo photosDeSantis speaks from Surfside: Community outpouring has been moving Biden opens up about grief at Surfside collapse visitMan avoids condo collapse after girlfriend requests he stay with herShe sued condo in 2015. Why her attorney remained worriedTeen says saving elderly woman was 'a blessing in disguise'Hear daughter's heartbreaking answer when asked if she wants to meet with BidenCondo owners were facing $15M in assessments for building repairsFamily says they found grandmother's photos, birthday card in debrisCouple explains why they aren't leaving sister tower of collapsed condo'It's not enough!': Frustrated mom lashes out at Florida officials Children of missing woman say dad was out of town when condo collapsedStructural engineer discusses concerns raised in 2018 reportEngineer raised concerns about structural damage at Surfside condominium in 2018 reportHear story of woman missing 7 family members in condo collapse$5M lawsuit filed against association of collapsed Florida building'Have hope': Hear fire chief's emotional message to familiesJUST WATCHEDVideo shows demolition of remainder of Surfside buildingReplayMore Videos ...MUST WATCH (CNN)Ten more bodies were found in the rubble of a condo collapse in Surfside, Florida, pushing the confirmed death toll to 46 -- with another 94 people still unaccounted for, Miami-Dade Mayor Daniella Levine Cava said Wednesday."As the magnitude of this catastrophe continues to grow each and every day since the collapse, our community and the world are grieving with all of the families who are living through this unthinkable tragedy," she said.Search and rescue efforts to find survivors amid the rubble of the building have become increasingly grim. Miami-Dade Fire Chief Alan Cominsky said Wednesday that search and rescue personnel combing the rubble have found no evidence that anyone survived the initial collapse.A day earlier, he said there had been no signs of any voids or livable spaces amid the wreckage where people might have survived."We're definitely searching," he said. "We're not coming across that."Read MoreOn Wednesday afternoon, a group of collapse survivors gathered at a local hotel to receive a multiple police vehicle escort back to the collapse site. The cluster of survivors gathered in the lobby of the hotel, being advised by uniformed police offers, officers in plain clothes, red cross workers and what appeared to be grief counselors.A woman in her sixties said she was heading back to the Champlain South collapse site. "I'm just sad, but I want to see it," she told CNN.The search continued Wednesday through inclement weather from Tropical Storm Elsa, which passed by the opposite coast of Florida. Winds of up to 30 miles per hour walloped crews Tuesday, but the weather had largely cleared by midday Wednesday, Cava said.Rescue crews battle storms as they search for dozens still unaccounted for in Florida condo collapseThe condo's collapse has raised questions about whether other residential structures could be at risk in Miami-Dade County, where sea levels are rising, the salty air is corrosive and nearly two-thirds of all commercial, condo and apartment buildings are as old or older than the 40-year-old building that collapsed, according to a CNN analysis of county records.Florida's legal community has created a safety task force to review laws governing the state's condominium development industry in the wake of the catastrophic collapse of a condo building in Miami-Dade County two weeks ago, according to a statement Tuesday.The Condominium Law and Policy on Life Safety Task Force is intended to serve residents of the state and was created by the Real Property, Probate, and Trust Law Section of the Florida Bar, according to the statement."The Task Force will serve as a resource to the Governor and Legislature as they review all aspects of Florida condominium law, development, association operations, and maintenance to determine and recommend if legislative and or regulatory changes should be enacted to minimize the likelihood of a similar tragedy," Bob Swain, chairperson of the Florida Bar Real Property, Probate, and Trust Law Section, said in a statement.How to help Surfside VictimsTeams not finding anything positive, but still more space to search Photos: Deadly condo collapse near MiamiRescue crews work at the site of the collapsed building in Surfside, Florida, on Tuesday, July 6. Hide Caption 1 of 53 Photos: Deadly condo collapse near MiamiMembers of a search-and-rescue team comb through the debris on Monday.Hide Caption 2 of 53 Photos: Deadly condo collapse near MiamiA memorial is seen near the spot where the building used to be. The rest of the building was demolished Sunday so that authorities could continue to look for survivors safely, officials said.Hide Caption 3 of 53 Photos: Deadly condo collapse near MiamiA controlled explosion brings down the unstable remains
    of the building on Sunday.Hide Caption 4 of 53 Photos: Deadly condo collapse near MiamiA woman cries as she watches the rest of Champlain Towers South be demolished.Hide Caption 5 of 53 Photos: Deadly condo collapse near MiamiPeople watch a cloud of dust form as the rest of the building is demolished.Hide Caption 6 of 53 Photos: Deadly condo collapse near MiamiKarol Casper places a flower on the memorial wall set up near the building on Sunday.Hide Caption 7 of 53 Photos: Deadly condo collapse near MiamiPeople stop at a makeshift memorial near the site.Hide Caption 8 of 53 Photos: Deadly condo collapse near MiamiSearch-and-rescue personnel work at the site on Friday.Hide Caption 9 of 53 Photos: Deadly condo collapse near MiamiResidents of the Crestview Towers Condominium carry their belongings as they leave their building in North Miami Beach, Florida, on Friday. The building, about 6 miles from Surfside, was deemed to be structurally and electrically unsafe based on a delinquent recertification report for the almost 50-year-old building. The city said the move was out of an "abundance of caution," as area authorities check high-rise condo buildings following the Surfside collapse.Hide Caption 10 of 53 Photos: Deadly condo collapse near MiamiPresident Joe Biden and first lady Jill Biden visit a memorial near the partially collapsed building on Thursday. Biden traveled to Surfside to console families still waiting on news of their loved ones. Those meetings were closed to the press.Hide Caption 11 of 53 Photos: Deadly condo collapse near MiamiA Coast Guard boat patrols the water ahead of Biden's visit on Thursday.Hide Caption 12 of 53 Photos: Deadly condo collapse near MiamiNBA basketball player Udonis Haslem, left, and Miami-Dade County Mayor Daniella Levine Cava arrive to pay their respects at a memorial near the building on June 30.Hide Caption 13 of 53 Photos: Deadly condo collapse near MiamiSearch-and-rescue teams look through the rubble of Champlain Towers South on June 29.Hide Caption 14 of 53 Photos: Deadly condo collapse near MiamiPeople take part in a twilight vigil near the building on June 28.Hide Caption 15 of 53
    Photos: Deadly condo collapse near MiamiMembers of the Legendarios, a men's religious group, gather near the building for a moment of prayer.Hide Caption 16 of 53 Photos: Deadly condo collapse near MiamiMore than 3 million pounds of concrete have already been removed during the rescue operation, said Miami-Dade Fire Chief Alan Cominsky.Hide Caption 17 of 53 Photos: Deadly condo collapse near MiamiA woman puts flowers in a barricade as she pays her respects near the building.Hide Caption 18 of 53 Photos: Deadly condo collapse near MiamiPassersby look at photos of missing people.Hide Caption 19 of 53 Photos: Deadly condo collapse near MiamiWorkers search through the rubble on June 26.Hide Caption 20 of 53 Photos: Deadly condo collapse near MiamiEliagne Sanchez and K. Parker lay flowers on the beach near the partially collapsed building.Hide Caption 21 of 53 Photos: Deadly condo collapse near MiamiSmoke rises as rescuers continued to search for survivors on June 26.Hide Caption 22 of 53 Photos: Deadly condo collapse near MiamiPeople stand near the building on June 25.Hide Caption 23 of 53 Photos: Deadly condo collapse near MiamiMourners light candles on the beach near the building.Hide Caption 24 of 53 Photos: Deadly condo collapse near MiamiMembers of a search-and-rescue team work in the rubble.Hide Caption 25 of 53 Photos: Deadly condo collapse near MiamiPeople pray together on the beach near the collapsed building.Hide Caption 26 of 53 Photos: Deadly condo collapse near MiamiFirefighters battle a blaze at the collapse site.Hide Caption 27 of 53 Photos: Deadly condo collapse near MiamiPeople hug June 25 as they wait for news about their relatives at a community center in Surfside.Hide Caption 28 of 53 Photos: Deadly condo collapse near MiamiRescue personnel search through the building's rubble on June 25.Hide Caption 29 of
    53 Photos: Deadly condo collapse near MiamiToby Fried holds up a picture of her missing brother, Chaim Rosenberg, outside the Surfside Community Center on June 25.Hide Caption 30 of 53 Photos: Deadly condo collapse near MiamiRescue workers use a crane to inspect the damage.Hide Caption 31 of 53 Photos: Deadly condo collapse near MiamiAriana Hevia, center, stands with Sean Wilt near the partially collapsed building on June 25. Hevia's mother, Cassandra Statton, lives in the building.Hide Caption 32 of 53 Photos: Deadly condo collapse near MiamiRescue workers arrive to the scene with dogs on June 25.Hide Caption
    33 of 53 Photos: Deadly condo collapse near MiamiFaydah Bushnaq, center, is hugged by Maria Fernanda Martinez as they stand on the beach near the building. Bushnaq, who was vacationing in South Florida, stopped to write "pray for their souls" in the sand.Hide Caption 34 of 53 Photos: Deadly condo collapse near MiamiThe arm of an earth mover is seen during the search operations.Hide Caption 35 of 53 Photos: Deadly condo collapse near MiamiRescue personnel work at the site on June 24.Hide Caption 36 of 53 Photos: Deadly condo collapse near MiamiYube Pettingill talks to the media. Two of her family members were still missing.Hide Caption 37 of 53 Photos: Deadly condo collapse near MiamiThis photo was tweeted by Miami-Dade Fire Rescue after the building collapsed.Hide Caption 38 of 53 Photos: Deadly condo collapse near MiamiDisplaced residents are taken to a nearby hotel in Surfside.Hide Caption 39 of 53 Photos: Deadly condo collapse near MiamiThe partial collapse left huge piles of rubble and materials dangling from what remained of the structure.Hide Caption 40 of 53 Photos: Deadly condo collapse near MiamiFlorida Gov. Ron DeSantis, at center in the red tie, arrives to speak to the media on June 24. "We still have hope to be able to identify additional survivors," DeSantis told reporters near the scene. "The state of Florida, we're offering any assistance that we can."Hide Caption 41 of 53 Photos: Deadly condo collapse near MiamiDebris dangles from the building on June 24.Hide Caption 42 of 53 Photos: Deadly condo collapse near MiamiPeople hug at a family reunification center where evacuees were staying in Surfside.Hide Caption 43 of 53 Photos: Deadly condo collapse near MiamiThe cause of the collapse wasn't immediately known.Hide Caption 44 of 53 Photos: Deadly condo collapse near MiamiJennifer Carr sits with her daughter as they and other evacuees wait for news at the family reunification center in Surfside.Hide Caption 45 of 53 Photos: Deadly condo collapse near MiamiRescue personnel search through the rubble with dogs.Hide Caption 46 of 53 Photos: Deadly condo collapse near MiamiPolice stand guard on the day the building collapsed.Hide Caption 47 of 53 Photos: Deadly condo collapse near MiamiPeople on the beach look at the building after the partial collapse.Hide Caption 48 of 53 Photos: Deadly condo collapse near MiamiThe building was constructed in 1981, according to online Miami-Dade property records.Hide Caption 49 of 53 Photos: Deadly condo collapse near MiamiPeople lie on cots at the family reunification center in Surfside.Hide Caption 50 of 53 Photos: Deadly condo collapse near MiamiThe beachfront community is a few miles north of Miami Beach.Hide Caption 51 of 53 Photos: Deadly condo collapse near MiamiMore than 80 rescue units responded to the scene, Miami-Dade Fire Rescue said.Hide Caption 52 of 53 Photos: Deadly condo collapse near MiamiRescue personnel work at the site of the partial collapse.Hide Caption 53 of 53Officials have said that despite the time that has passed, they remain hopeful they will still find survivors. The key to finding survivors, Cominsky said, is finding voids or livable spaces among the rubble.About 5 million pounds of debris have been removed from the site so far, Cominsky said. But with the amount of ground to cover, there is no telling what the teams will find in the coming days, Cominsky said.The site has been broken up into grids, none of which have been fully cleared yet. The way the building collapsed as well as the magnitude of it means that teams have been able to get further down on some areas than others so far, he said.A college student, the daughter of a Miami firefighter, a family of four: What we know about the collapse victimsTeams continue to search "as aggressive as we can to see if we can assist with the families and locate individuals," he said. Tuesday was a day of gratitude for one family, when the uncle of a 15-year-old called the man who pulled the boy from the rubble just after the collapse to thank him.Nicholas Balboa told CNN on Tuesday that he heard 15-year-old Jonah Handler screaming under the rubble after the condo building collapsed. Balboa was not in the building but was standing nearby when it collapsed. Balboa said Jonah's uncle told him Jonah was out of the hospital with only minor injuries. Since the collapse, Balboa says he has replayed that moment in his mind many times, wondering what he could have done differently to save more people, he said. Four additional bodies were recovered Tuesday, Levine Cava said. The victims of the collapse range in age from 4 to 92.With rescue
    efforts still underway, some families have asked to visit the collapse site, Surfside Mayor Charles Burkett said."Of course, we have to work around the rescue efforts," he said. "I think it would be very, very good for those families to again see the amazing efforts that are being expended on their behalf."
    Debris held for investigationSearch and rescue teams continue to work in the rubble at the site of the collapsed Champlain Towers South condo in Surfside.Meanwhile, more federal organizations are investigating why the building collapsed. Mayor Levine Cava said the National Institute of Standards and Technology (NIST), the US Geological Survey and the National Science Foundation are sending staff."NIST, our federal partner, continues to work closely with the structural specialists, with detectives, and the fire rescue crews on site, as the evidence gathering process is well underway," she said."They're capturing all possible insights from the debris and all evidence is being properly tagged and logged."'Tragedy beyond tragedy': Champlain Towers South was a catastrophe in slow motion All of the debris removed from the site is considered "evidentiary debris," Levine Cava said. The remnants are being sorted on-site, and any objects that can be distinguished are put in certain bins and labeled as to their exact location, the mayor said.The county has created a form for family members to document their belongings, which will be an active part of the investigation, Levine Cava said."The families are not reviewing what's come out of the site at this time, but we have photographs, they have their information, and as we move forward, we'll be attempting to do matching and releasing it to them as soon as we can, given the active investigation," she said.CNN's Rosa Flores, John Couwels, Amanda Watts, Rebekah Riess, Leyla Santiago,
    Gregory Lemos, David Shortell, Curt Devine and Paul Vercammen contributed to this report.</p></body></html>
    """
    p = printPDF(t, r"C:/Users/chitg/Desktop/")
