REM - This script moves the relevant .sav and .ini files that UE4 internally references to the new folder that the engine wants for the shipping build configuration of the game.
REM - If for some reason the Steam auto install failed to copy the save/config files over, you can run this one manually.

mkdir %localappdata%\FPSAimTrainer\Saved\Config\WindowsNoEditor
mkdir %localappdata%\FPSAimTrainer\Saved\SaveGames

move /Y ..\..\FPSAimTrainer\Saved\Config\WindowsNoEditor\*.ini %localappdata%\FPSAimTrainer\Saved\Config\WindowsNoEditor
move /Y ..\..\FPSAimTrainer\Saved\SaveGames\*.sav %localappdata%\FPSAimTrainer\Saved\SaveGames

REM and return 0 so that Steam knows this doesn't need to be run again.

exit /b 0