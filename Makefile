MY_VAR := ${shell python -c 'from pytgbot import VERSION as v; print(v)'}

clean:
	rm -rf *.so *.egg-info build *.png *.log *.svg

upload: clean
	python setup.py sdist
	@echo UPLOADING VERSION $(MY_VAR)
	twine upload dist/pytgbot-${MY_VAR}.tar.gz
