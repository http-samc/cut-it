from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from utils.resource import PATH

def getBrowser():

    chrome_options = Options()
    chrome_options.add_extension(PATH.get('bypass.crx'))
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--log-level=3")

    browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    html = """
        <html><head><title>AutoBypass</title></head><body>
        <h1>Welcome to Cut-It's AutoBypass Browser</h1>
        <p>We use a modified version of <a href='https://github.com/iamadamdev/bypass-paywalls-chrome/tree/1b18c8f7666e073b42332187e44c056095241189'>
        Bypass Paywalls</a> to give you functionality on paywalled sites that AutoCut can't reach. This browser starts clean every single time, so you
        don't need to worry about putting <em>sketchy</em> extensions on your Chrome profile. This works on nearly 200 different sites, including Bloomberg,
        The Chicago Tribune, Business Insider, Financial News, Foreign Policy, The Atlantic, The New York Times,
        The Wall Street Journal, The Washington Post, The Economist, and more. See the full list below! This is a normal Chrome browser - use it like one!</p>
        <p>
            Adweek<br>
            Algemeen Dagblad
            American Banker
            Ámbito
            Baltimore Sun
            Barron's
            Bloomberg Quint
            Bloomberg
            BN De Stem
            Boston Globe
            Brabants Dagblad
            Brisbane Times
            Business Insider
            Caixin
            Central Western Daily
            Chemical & Engineering News
            Chicago Tribune
            Corriere Della Sera
            Crain's Chicago Business
            Daily Press
            De Gelderlander
            De Groene Amsterdammer
            De Stentor
            De Speld
            De Tijd
            De Volkskrant
            DeMorgen
            Denver Post
            Diario Financiero
            Domani
            Dynamed Plus
            Eindhovens Dagblad
            El Mercurio
            El Pais
            El Periodico
            Elu24
            Encyclopedia Britannica
            Estadão
            Examiner
            Expansión
            Financial News
            Financial Post
            Financial Times
            First Things
            Foreign Policy
            Fortune
            Genomeweb
            Glassdoor
            Globes
            Grubstreet
            Haaretz.co.il
            Haaretz.com
            Handelsblatt
            Harper's Magazine
            Hartford Courant
            Harvard Business Review
            Herald Sun
            Het Financieel Dagblad
            History Extra
            Humo
            Il Manifesto
            Inc.com
            Interest.co.nz
            Investors Chronicle L'Écho
            L.A. Business Journal
            La Nación
            La Repubblica
            La Stampa
            La Tercera
            La Voix du Nord
            Le Devoir
            Le Parisien
            Les Échos
            Loeb Classical Library
            London Review of Books
            Los Angeles Times
            MIT Sloan Management Review
            MIT Technology Review
            Medium
            Medscape
            Mexicon News Daily
            Mountain View Voice
            New York Daily News
            NRC Handelsblad
            NT News
            National Post
            Neue Zürcher Zeitung
            New York Magazine
            New Zealand Herald
            Nikkei Asian Review
            Orange County Register
            Orlando Sentinel
            PZC
            Palo Alto Online
            Parool
            Postimees
            Quartz
            Quora
            Quotidiani Gelocal
            Republic.ru
            Reuters
            San Diego Union Tribune
            San Francisco Chronicle
            Scientific American
            Seeking Alpha
            Slate
            SOFREP
            Statista
            Star Tribune
            Stuff
            SunSentinel
            Tech in Asia
            Telegraaf
            The Advertiser
            The Advocate
            The Age
            The American Interest
            The Atlantic
            The Australian Financial Review
            The Australian
            The Business Journals
            The Canberra Times
            The Courier
            The Courier Mail
            The Cut
            The Daily Telegraph
            The Diplomat
            The Economist
            The Globe and Mail
            The Herald
            The Hindu
            The Irish Times
            The Japan Times
            The Kansas City Star
            The Mercury News
            The Mercury Tasmania
            The Morning Call
            The Nation
            The National
            The New Statesman
            The New York Times
            The New Yorker
            The News-Gazette
            The Philadelphia Inquirer
            The Saturday Paper
            The Seattle Times
            The Spectator Australia
            The Spectator
            The Sydney Morning Herald
            The Telegraph
            The Toronto Star
            The Wall Street Journal
            The Washington Post
            The Wrap
            TheMarker
            Times Literary Supplement
            Towards Data Science
            Trouw
            Tubantia
            Vanity Fair
            Vrij Nederland
            Vulture
            Winston-Salem Journal
            Wired
            World Politics Review
            Zeit Online
        <p>
        </body></html>
    """
    browser.execute_script(f"document.write(`{html}`)")

if __name__ == "__main__":
    getBrowser()