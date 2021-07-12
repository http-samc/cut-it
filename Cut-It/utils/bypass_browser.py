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
        <html><head><title>SuperBrowser</title></head><body>
        <h1>Welcome to Cut-It's Super Browser</h1>
        This browser gives you functionality on sites that AutoCut can't reach. It starts clean every single time and uses
        client side JS to clear cookies and allow access to nearly 200 different sites, including Bloomberg,
        The Chicago Tribune, Business Insider, Financial News, Foreign Policy, The Atlantic, The New York Times,
        The Wall Street Journal, The Washington Post, The Economist, and more. This functions like a normal Chrome browser - use it like one!
        <br><br><b><em> Unfortunately, we need to keep it legal, so this can't bypass hard paywalls!</em><b></p>
        </body></html>
    """
    browser.execute_script(f"document.write(`{html}`)")

if __name__ == "__main__":
    getBrowser()