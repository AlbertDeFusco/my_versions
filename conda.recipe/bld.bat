set MENU_DIR=%PREFIX%\Menu
mkdir %MENU_DIR%

set SCRIPT_DIR=%PREFIX%\Scripts
mkdir %SCRIPT_DIR%

copy %RECIPE_DIR%\menu-windows.json %MENU_DIR%\my_versions.json
if errorlevel 1 exit 1

%PYTHON% setup.py install
if errorlevel 1 exit 1

