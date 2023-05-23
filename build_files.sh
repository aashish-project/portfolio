
exho "BUILD START"
python3.10 -m pip install -r requirement.text
python3.10 manage.py collectsstatic --noimput --clear
exho "BUILD END"
