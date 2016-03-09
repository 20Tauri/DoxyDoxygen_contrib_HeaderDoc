
## DoxyDoxygen_contrib_HeaderDoc

This plugin adds HeaderDoc support to [DoxyDoxygen](https://github.com/20Tauri/DoxyDoxygen).
It can be used as a template to add you own documenting style to DoxyDoxygen.

To use them. First:

   - Install DoxyDoxygen.

Then:

   - Click the ```Preferences > Browse Packages...``` menu to open package directory
   - Create a directory named ```DoxyDoxygen_contrib_<your_module_name>```
   - Copy into it the content of ```DoxyDoxygen_contrib_HeaderDoc```
   - If installed from `Packages Control`, remove its added file `package-metadata.json`
   - Edit ```DocStyle.py``` according your need. ```DocStyle.py``` is located in a sub-folder giving the version of DoxyDoxygen interface used. Please preserve it.
   - Edit your DoxyDoxygen settings to use this style (ie: put ```DoxyDoxygen_contrib_<your_module_name>``` as DocStyle)
