echo off

:: USER CONFIGURATION OPTIONS
:: Choose the Conda environment you want to use (e.g., base, main, my_new_env). Default=base.
SET "MY_ENVIRONMENT=base"
:: Choose your directory path (the location of this file).
cd "C:\Users\hawkem\OneDrive - Office for National Statistics\Tools\Search"




set root=%USERPROFILE%/Anaconda3

call %root%/Scripts/activate.bat %root%

call activate "%MY_ENVIRONMENT%"

echo.
echo Your setup:
echo Environment "%MY_ENVIRONMENT%" at %CONDA_PREFIX% & python --version
echo cd %cd%
echo.

echo Checking required packages installed (see requirements.txt)...
pip install --no-input --quiet --user -r requirements.txt
echo.
pip show streamlit streamlit-keyup bokeh | findstr -i "version name"
echo.

start "" http://localhost:8501

streamlit run "%cd%/main.py"

cmd \k
