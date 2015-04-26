# vim:ft=make:
# -*- MakeFile -*-

.PHONY: deps build
.DEFAULT_GOAL := build

check-env:
ifndef TRAVIS
    $(error Not on TravisCI)
endif

install:
	python -m pip install -r .build_requirements.txt

deps:
	mkdir -p ./deps/AAAPackageDev
	wget -qO- https://github.com/SublimeText/AAAPackageDev/archive/1.0.6.tar.gz | tar xz -C ./deps/AAAPackageDev --strip-components=1

build:
	mkdir -p ./build
	./.build.py

print:
	echo ============================================================
	cat build/fgd.tmLanguage
	echo ============================================================

clean:
	git clean -df ./deps/ ./build/

