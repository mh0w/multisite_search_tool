# Multisite search tool

This tool allows the user to search several sites using one search bar.

Note that each site opens in a new tab or window, so you may need to tell your
browser's popup blocker to allow this tool to create popups (new tabs/windows).




**OPTIONAL** - user configuration: you can choose the Conda environment you want to use near the
top of the run.bat file. You can also declare your directory path here (where you
have placed the tool on your computer, e.g., C:/desktop/search_tool).

**OPTIONAL** - add sites: you can add sites to search by adding them to the sites_list list in
the main.py file. Use the same format as the sites already listed. Make sure
you include http:// or https://. For example, you could add the following line:
`"Bing": "https://www.bing.com/search?q=SEARCH_TEXT_HERE",`
