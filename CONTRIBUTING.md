# Contributing Policy
If you are interested in contributing to the codebase, you must adhere to the following guidelines:
- Open an ``Issue`` to discuss what changes you'd like to make
- If approved by a *Project Manager*, we'd be interested in integrating the feature into the codebase
  - Keep in mind that even if we don't see the need for the feature, you're more than welcome (per our license) to fork the repository and write your own version
- After writing the code, you can make a ``Pull Request``
- If approved, your code will be automatically integrated into the program, and distributed the following release cycle
- The following stipulations apply:
  - **No** guarentee is made regarding the approval of a ``Pull Request``, regardless of whether or not the ``Issue`` was initially approved
  - **No** guarentee is made that explicit credit will be given in the program itself (all contributers are auto-added to the [contributors section](https://github.com/http-samc/cut-it/graphs/contributors))
  - *The Project Managers* reserve the right to reject any pull request **for any reason, with or without explanation**
  - ***Any and every instance of homophobia, racism, sexism, or another practice deemed offensive by the Project Managers will immediately result in a ban on your ability to contribute to the codebase.***

# Contributing FAQ
Here are some quick basics about the project:
- The codebase is in Python 3.X, and the GUI interface used is PyQt. These are mainstays of the codebase and thus will not likely be changed by any requested PRs.
- The app is designed to be deployed on Windows and MacOS.
- The Utils folder contains various API resources that enable Cut-It's functionality. A short description of each class is found at the top of their respective files.
- ``app.py`` is the main file, and is what the build is based off of. Any time a binary is generated, a *temporary* ``app.py`` is generated with the converted UI code to avoid bundling raw UI files.
- If you'd like to contribute but don't have any ideas, feel free to check the ``Issues`` tab and filter for the ``Enhancement`` tag, which will show you uncoded TODOs.

# Any questions?
Contact [Samarth Chitgopekar](mailto:sam@chitgopekar.tech)!