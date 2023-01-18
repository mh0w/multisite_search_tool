# Multisite search tool

This tool allows the user to search several sites using one search bar.

Note that each site opens in a new tab or window, so you may need to tell your
browser's popup blocker to allow this tool to create popups (new tabs/windows).

You will need to install any missing required packages, such as by running the
run.bat file if you have pip setup.

Open the multisite search tool by running the run.bat file. This will
install any missing required packages (using `pip install`) and open the search tool.


**OPTIONAL**: you can choose the Conda environment you want to use near the
top of the run.bat file. 

**OPTIONAL**: you can declare your directory path (where you
have placed the tool on your computer, e.g., C:/desktop/search_tool)
near the top of the run.bat file.

**OPTIONAL**: you can add sites to search by adding them to the sites_list list in
the main.py file. Use the same format as the sites already listed. Make sure
you include http:// or https://. For example, you could add the following line:
`"Bing": "https://www.bing.com/search?q=SEARCH_TEXT_HERE",`. Notice that
SEARCH_TEXT_HERE indicates where your search phrase will go. An easy way to
prepare a URL in a suitable format is to search SEARCH_TEXT_HERE in the
search engine you want to add, such as in Bing. If you go to
https://www.bing.com/search?q=SEARCH_TEXT_HERE you will notice that this is
a Bing search for SEARCH_TEXT_HERE.

![image](https://user-images.githubusercontent.com/82766547/213148208-303de395-7156-4f64-9b6b-7b41578fe4ef.png)
