REM - This script moves the relevant .sav and .ini files that UE4 internally references to the new folder that the engine wants for the shipping build configuration of the game.
REM - Steam should run this once then set a registry key and not bother running it again.

mkdir %localappdata%\FPSAimTrainer\Saved\Config\WindowsNoEditor
mkdir %localappdata%\FPSAimTrainer\Saved\SaveGames

REM Note that the path to the below files are referenced from the main install folder of the game.  This script is run once by Steam and not intended to be run manually (you'd need to move it to where FPSAimTrainer.exe resides and run it there).

move /Y FPSAimTrainer\Saved\Config\WindowsNoEditor\*.ini %localappdata%\FPSAimTrainer\Saved\Config\WindowsNoEditor
move /Y FPSAimTrainer\Saved\SaveGames\*.sav %localappdata%\FPSAimTrainer\Saved\SaveGames

REM and return 0 so that Steam knows this doesn't need to be run again.

exit /b 0