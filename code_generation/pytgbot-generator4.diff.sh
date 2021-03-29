cd /


cd /pytgbot/

# cp __init__.py code_generation/output/pytgbot/__init__.py
find . -maxdepth 5 \( ! -type d \) -exec sh -c 'echo cp  "$@" "../code_generation/output/pytgbot/$@"' _ {} \;
# non-dry-run:
find . -maxdepth 5 \( ! -type d \) -exec sh -c 'cp  "$@" "../code_generation/output/pytgbot/$@"' _ {} \;
# cp ./__init__.py code_generation/output/pytgbot/./__init__.py

cd code_generation/output/pytgbot/

git diff . > ../../pytgbot-generator4.patch

