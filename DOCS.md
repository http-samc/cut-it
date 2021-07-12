`Cut-It` **1.0@Release**
## [Cut-It.app.py](/Cut-It/app.py)
---
### Cut-It.app.`main` [class] [inherits: `GUI`]
Adds logic to the GUI class
<details style='color: #333333'><summary>Methods</summary><p>

#### main.`__init__`
No Documentation Provided
#### main.`_updater_`
```Python
Determines whether to present an update window
```
#### main.`_autoBypass`
```Python
Generates Bypassed Browser
```
#### main.`_loadSettings`
```Python
Loads all user data into instance vars
Fills in UI with Settings if initialLoad
```
#### main.`__loadSettingsUI`
```Python
Loads the Settings into the GUI
```
#### main.`_updateShortcut`
```Python
Updates shortcut when user wants to view a separate one
```
#### main.`_saveShortcut`
```Python
Saves shortcut to memory when user is done editing
```
#### main.`_loadShortcuts`
```Python
Inits custom keybindings for all user-defined shortcuts
```
#### main.`_saveSettings`
```Python
Saves settings to data.json
```
#### main.`_updates`
```Python
Changes text of button to notify if update is needed or not
```
#### main.`_feedback`
```Python
Submits feedback
```
#### main.`_toggleTheme`
```Python
Changes theme from current to reciprocal (applies on reboot)
(eg. light -> dark, dark -> light)
```
#### main.`_addDelimiter`
```Python
Triggered when the evidence box's text changes
Adds closing bracket ] when an opening one [ is typed
```
#### main.`_toHTML`
```Python
Returns list: [text of card, html of card]
Copies plain & rich text to clipboard IFF :param: copy -> True
```
#### main.`_auto`
```Python
Adds MLA & Debate-Grade Citation and/or article text to evidence box
```
#### main.`_copy`
```Python
Copies card to clipboard
```
#### main.`_onClose`
```Python
Behavior for window close (saves card first)
```
#### main.`_tabChanged`
```Python
Saves settings and reapplies them on tab change
```
#### main.`_log`
```Python
Posts card objs to API for efficacy monitoring & paywall enforcement
& GitHub badge stats
```
#### main.`__loadAllCards`
```Python
Adds all cards to card history selector
```
#### main.`_saveCard`
```Python
Saves current card if it has data (is not blank)
```
#### main.`_newCard`
```Python
Saves old card and opens new one
```
#### main.`_loadCard`
```Python
Loads most recent card (saves previous one as well and adds to card selector)
```
#### main.`_deleteCard`
```Python
Deletes currently open card after second click for safety
```
#### main.`_addToCardSelector`
```Python
Adds current card to card selector
```
#### main.`_cardSelectionChanged`
```Python
Resets the delete status (clicked once) if the selected card changes
```
#### main.`_autoCiteAndPoll`
```Python
Adds MLA & Debate-Grade Citation & article text to evidence box
```
#### main.`_autoCite`
```Python
Adds MLA & Debate-Grade Citation to evidence box
```
#### main.`_autoPoll`
```Python
Adds article text to evidence box
```
#### main.`_print`
```Python
Triggers User Input for Directory and Saves Card as PDF
```
#### main.`__getSelectedText`
```Python
Returns cursor's start index and currently selected text in a tuple
```
#### main.`__addText`
```Python
Inserts formatted text at cursor position and reselects text
Copies text to clipboard
```
#### main.`_primaryEmphasis`
```Python
Styles text with Primary Emphasis
```
#### main.`_secondaryEmphasis`
```Python
Styles text with Secondary Emphasis
```
#### main.`_tertiaryEmphasis`
```Python
Styles text with Tertiary Emphasis
```
#### main.`_highlightP`
```Python
Highlights text with Primary Highlight Color
```
#### main.`_highlightS`
```Python
Highlights text with Secondary Highlight Color
```
#### main.`_bold_`
```Python
Bolds selected text
```
#### main.`_underline_`
```Python
Underlines selected text
```
#### main.`_italic_`
```Python
Italicises selected text
```
#### main.`_clearFormatting`
```Python
Clears Formatting on selected text
```
#### main.`_minimizeText`
```Python
Minimizes Text
```
#### main.`_bold`
```Python
Returns bolded version of :param: text
```
#### main.`_underline`
```Python
Returns underlined version of :param: text
```
#### main.`_italic`
```Python
Returns italicised version of :param: text
```
#### main.`_highlight`
```Python
Returns highlighted version of :param: text of the color :param: color
```
</p></details>

## [Cut-It.GUI.py](/Cut-It/GUI.py)
---
### Cut-It.GUI.`GUI` [class] [inherits: `MainWindow`]
No Documentation Provided
<details style='color: #333333'><summary>Methods</summary><p>

#### GUI.`__init__`
```Python
Loads latest UI
```
#### GUI.`addCardHistory`
```Python
Manually fill out the Card History groupBox (due to custom widgets)
```
#### GUI.`updateStyling`
No Documentation Provided
#### GUI.`addToolTips`
```Python
Adds in ToolTips
```
#### GUI.`addAttrs`
```Python
Adds in missing attrs.
```
#### GUI.`addDistroDetails`
```Python
Returns a formatted String to be inserted into the Distro box in the about section
```
</p></details>

## [Cut-It.install.py](/Cut-It/install.py)
---
### Cut-It.install.`install` [function]
No Documentation Provided
## [Cut-It.utils.bypass_browser.py](/Cut-It/utils/bypass_browser.py)
---
### Cut-It.utils.bypass_browser.`getBrowser` [function]
No Documentation Provided
## [Cut-It.utils.card.py](/Cut-It/utils/card.py)
---
### Cut-It.utils.card.`Card` [class]
No Documentation Provided
<details style='color: #333333'><summary>Methods</summary><p>

#### Card.`isCard`
```Python
Returns (bool) if the card actually has data
```
#### Card.`getDict`
```Python
Returns (dict) representation of the object
```
</p></details>


## [Cut-It.utils.citer.py](/Cut-It/utils/citer.py)
---
### Cut-It.utils.citer.`cite` [class]
No Documentation Provided
<details style='color: #333333'><summary>Methods</summary><p>

#### cite.`__init__`
```Python
:param: URL (str) - the URL for your citation
:desc: creates citation
```
#### cite.`cite`
```Python
gets raw citation data from API
```
#### cite.`format`
```Python
formats raw citation date
```
#### cite.`getMissingAttrs`
```Python
Returns a list of missing attributes (key) or None (if all present)
```
#### cite.`debate`
```Python
Returns a simplified debate-ready citation
```
#### cite.`mla`
```Python
Returns an MLA 8 citation
```
</p></details>

## [Cut-It.utils.clipboard_OSX.py](/Cut-It/utils/clipboard_OSX.py)
---
### Cut-It.utils.clipboard_OSX.`clipboard` [class]
No Documentation Provided
<details style='color: #333333'><summary>Methods</summary><p>

#### clipboard.`add`
```Python
Injects both regular text (unformatted)
and html ('rich' text) to clipboard
```
</p></details>

## [Cut-It.utils.clipboard_WIN.py](/Cut-It/utils/clipboard_WIN.py)
---
### Cut-It.utils.clipboard_WIN.`clipboard` [class]
No Documentation Provided
<details style='color: #333333'><summary>Methods</summary><p>

#### clipboard.`add`
```Python
Injects both regular text (unformatted)
and html ('rich' text) to clipboard
```
</p></details>

## [Cut-It.utils.data.py](/Cut-It/utils/data.py)
---
### Cut-It.utils.data.`init` [function]
```Python
Initializes both Card and Preferences storage
```
### Cut-It.utils.data.`getIndex` [function]
```Python
Returns (int) current card index
```
### Cut-It.utils.data.`setIndex` [function]
```Python
Sets the stored card index
```
### Cut-It.utils.data.`getPrefData` [function]
```Python
Returns a dict of data.json
```
### Cut-It.utils.data.`setPrefData` [function]
```Python
Writes to data.json
```
### Cut-It.utils.data.`getPref` [function]
```Python
Returns the value of the inputted preference key
```
### Cut-It.utils.data.`setPref` [function]
```Python
Sets the value of the inputted preference key to the
inputted value
```
### Cut-It.utils.data.`getShort` [function]
```Python
Returns the value of the inputted shortcut key
```
### Cut-It.utils.data.`setShort` [function]
```Python
Sets the value of the inputted shortcut key to the
inputted value
```
### Cut-It.utils.data.`getCardData` [function]
```Python
Returns a dict of cards.json
```
### Cut-It.utils.data.`setCardData` [function]
```Python
Writes to cards.json
```
### Cut-It.utils.data.`getCard` [function]
```Python
Returns card at start OR at supplied index
```
### Cut-It.utils.data.`addCard` [function]
```Python
Checks if a card contains information, if so adds it
to the end of cards.json, or if an index is
supplied it will overwrite the card at that pos
```
### Cut-It.utils.data.`deleteCard` [function]
```Python
Deletes card at specified index
```
## [Cut-It.utils.distro.py](/Cut-It/utils/distro.py)
---
### Cut-It.utils.distro.`version` [function]
```Python
Returns current software version
```
### Cut-It.utils.distro.`tag` [function]
```Python
Returns current software tag
```
### Cut-It.utils.distro.`releases` [function]
```Python
Returns GitHub API Releases URL
```
## [Cut-It.utils.export.py](/Cut-It/utils/export.py)
---
### Cut-It.utils.export.`printPDF` [function]
```Python
Saves html to pdf with Selenium

Args:
    body (str): the "body" section of the html
    path (str): path to the save folder
    cardName (str, optional): the name of the card (becomes filename). Defaults to "Cut-It Export".
```
## [Cut-It.utils.ext_combobox.py](/Cut-It/utils/ext_combobox.py)
---
### Cut-It.utils.ext_combobox.`ExtendedComboBox` [class] [inherits: `QComboBox`]
No Documentation Provided
<details style='color: #333333'><summary>Methods</summary><p>

#### ExtendedComboBox.`__init__`
No Documentation Provided
#### ExtendedComboBox.`goToStart`
No Documentation Provided
#### ExtendedComboBox.`on_completer_activated`
No Documentation Provided
#### ExtendedComboBox.`setModel`
No Documentation Provided
#### ExtendedComboBox.`setModelColumn`
No Documentation Provided
</p></details>

## [Cut-It.utils.feedback.py](/Cut-It/utils/feedback.py)
---
### Cut-It.utils.feedback.`send_feedback` [function]
No Documentation Provided
## [Cut-It.utils.MainWindow.py](/Cut-It/utils/MainWindow.py)
---
### Cut-It.utils.MainWindow.`MainWindow` [class] [inherits: `QMainWindow`]
No Documentation Provided
<details style='color: #333333'><summary>Methods</summary><p>

#### MainWindow.`__init__`
No Documentation Provided
#### MainWindow.`retranslateUi`
No Documentation Provided
</p></details>

## [Cut-It.utils.resource.py](/Cut-It/utils/resource.py)
---
### Cut-It.utils.resource.`PATH` [class]
No Documentation Provided
<details style='color: #333333'><summary>Methods</summary><p>

#### PATH.`get`
```Python
returns path for included files
(used when packaged into a binary)
```
</p></details>

## [Cut-It.utils.text_scraper.py](/Cut-It/utils/text_scraper.py)
---
### Cut-It.utils.text_scraper.`text` [class]
No Documentation Provided
<details style='color: #333333'><summary>Methods</summary><p>

#### text.`scrape`
No Documentation Provided
</p></details>

## [Cut-It.utils.UpdateDialog.py](/Cut-It/utils/UpdateDialog.py)
---
### Cut-It.utils.UpdateDialog.`UpdateDialog` [class] [inherits: `QDialog`]
No Documentation Provided
<details style='color: #333333'><summary>Methods</summary><p>

#### UpdateDialog.`__init__`
No Documentation Provided
#### UpdateDialog.`retranslateUi`
No Documentation Provided
</p></details>

## [Cut-It.utils.updater.py](/Cut-It/utils/updater.py)
---
### Cut-It.utils.updater.`Updater` [class] [inherits: `UpdateDialog`]
No Documentation Provided
<details style='color: #333333'><summary>Methods</summary><p>

#### Updater.`__init__`
```Python
Loads latest UI
```
#### Updater.`addOptions`
```Python
Adds data about an update, if any
```
#### Updater.`getUpdate`
```Python
Opens download URL in Selenium Chrome
```
#### Updater.`_quit`
No Documentation Provided
#### Updater.`_close`
No Documentation Provided
</p></details>

## [Cut-It.utils.version_check.py](/Cut-It/utils/version_check.py)
---
### Cut-It.utils.version_check.`pollReleases` [function]
```Python
Searches GitHub Releases for new version of matching tag
```
### Cut-It.utils.version_check.`check` [function]
No Documentation Provided
