SET logfile="C:\Users\Documents\Gareth\Scraper\log.txt"
@echo off
@echo Starting Script at %date% %time% >> %logfile%
call C:\Users\anaconda3\condabin\activate "C:\Users\anaconda3\envs\conda_env"
python "C:\Users\Documents\Gareth\Scraper\scraper.py"
@echo finished at %date% %time% >> %logfile%
PAUSE