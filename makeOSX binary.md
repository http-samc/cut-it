These are the Windows Config Options: \
Step 1: Use the API for OSX (comment out the line that is noted on the app.py file) \
Step 2: Install all requirements \
Step 3: Use the Config below, Note: Everything has a **PATH TO** (only relative paths are shown here) (eg. C:/PATH/TO/Cut-IT + the relative path shown here)

```
{
 "pyinstallerOptions": [
  {
   "optionDest": "noconfirm",
   "value": true
  },
  {
   "optionDest": "filenames",
   "value": "app.py"
  },
  {
   "optionDest": "onefile",
   "value": false
  },
  {
   "optionDest": "console",
   "value": false
  },
  {
   "optionDest": "icon_file",
   "value": "/resources/otr_icon.ico"
  },
  {
   "optionDest": "ascii",
   "value": false
  },
  {
   "optionDest": "clean_build",
   "value": false
  },
  {
   "optionDest": "strip",
   "value": false
  },
  {
   "optionDest": "noupx",
   "value": false
  },
  {
   "optionDest": "uac_admin",
   "value": false
  },
  {
   "optionDest": "uac_uiaccess",
   "value": false
  },
  {
   "optionDest": "win_private_assemblies",
   "value": false
  },
  {
   "optionDest": "win_no_prefer_redirects",
   "value": false
  },
  {
   "optionDest": "bootloader_ignore_signals",
   "value": false
  },
  {
   "optionDest": "datas",
   "value": "/resources;resources/"
  }
 ],
 "nonPyinstallerOptions": {
  "increaseRecursionLimit": true,
  "manualArguments": ""
 }
}
```