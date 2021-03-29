
cd code_generation/output/pytgbot/
git apply ../../pytgbot-generator-patch.patch

#  cp api_types/__init__.py ../../../pytgbot/api_types/__init__.py
find . -maxdepth 5 \( ! -type d \) -exec sh -c 'echo cp  "$@" "../../../pytgbot/$@"' _ {} \;
# non-dry-run:
find . -maxdepth 5 \( ! -type d \) -exec sh -c 'cp  "$@" "../../../pytgbot/$@"' _ {} \;
#  cp ./api_types/__init__.py ../../../pytgbot/./api_types/__init__.py

git apply -R ../../pytgbot-generator-patch.patch
