
duckuments-branch=master
dist_dir=duckuments-dist/$(duckuments-branch)

out_html=$(dist_dir)/duckiebook.html
out_html2=$(dist_dir)/duckiebook_pdf.html
out_pdf=$(dist_dir)/duckiebook.pdf

tex-symbols=docs/symbols.tex
duckietown-software=duckietown

src="docs:$(duckietown-software)/catkin_ws/src:$(duckietown-software)/Makefiles"

all:
	ONLY_FOR_REFS=1 make books
	make books

realclean: clean
	rm -rf duckuments-dist

.PHONY: $(out_html) checks check-duckietown-software check-programs

.PHONY: builds

builds:
	python -m mcdp_docs.sync_from_circle duckietown duckuments builds builds/duckuments.html


checks: check-duckietown-software check-programs

check-programs-pdf:
	@which  pdftk >/dev/null || ( \
		echo "You need to install pdftk."; \
		exit 1)

check-programs:
	@which  bibtex2html >/dev/null || ( \
		echo "You need to install bibtex2html."; \
		exit 2)

	@which  mcdp-render >/dev/null  || ( \
		echo "The program mcdp-render is not found"; \
		echo "You are not in the virtual environment."; \
		exit 3)

	@which  mcdp-split >/dev/null  || ( \
		echo "The program mcdp-split is not found"; \
		echo "You need to run 'python setup.py develop' from mcdp/."; \
		exit 4)

	@which  convert >/dev/null  || ( \
		echo "You need to install ImageMagick"; \
		exit 2)

	@which  gs >/dev/null  || ( \
		echo "You need to install Ghostscript (used by ImageMagick)."; \
		exit 2)

	@echo All programs installed.

check-duckietown-software:
	@if [ -d $(duckietown-software) ] ; \
	then \
	     echo '';\
	else \
		echo 'Please create a link "$(duckietown-software)" to the Software repository.'; \
		echo '(This is used to include the package documentation)'; \
		echo ''; \
		echo 'Assuming the usual layout, this is:'; \
		echo '      ln -s  ~/duckietown $(duckietown-software)'; \
		echo ''; \
		exit 1; \
	fi;

generated_figs=docs/generated_pdf_fig

inkscape2=/Applications/Inkscape.app/Contents/Resources/bin/inkscape

process-svg-clean:
	-rm -f $(generated_figs)/*pdf

process-svg:
	@which  inkscape >/dev/null || which $(inkscape2) || ( \
		echo "You need to install inkscape."; \
		exit 2)
	@which  pdfcrop >/dev/null || (echo "You need to install pdfcrop."; exit 1)
	@which  pdflatex >/dev/null || (echo "You need to install pdflatex."; exit 1)


	python -m mcdp_docs.process_svg docs/ $(generated_figs) $(tex-symbols)


log=misc/bot/logs/generic.log
log-master-html=misc/bot/logs/master-html/compilation.log
log-master-pdf=misc/bot/logs/master-pdf/compilation.log
log-fall2017=misc/bot/logs/fall2017/compilation.log
log-fall2017-pdf=misc/bot/logs/fall2017-pdf/compilation.log

automatic-compile-cleanup:
	echo "\n\nautomatic-compile-cleanup killing everything" >> $(log)
	-killall -9 /home/duckietown/scm/duckuments/deploy/bin/python
	$(MAKE) master-clean
	$(MAKE) fall2017-clean
	rm -f misc/bot/locks/*
	rm -f /home/duckietown/scm/duckuments/duckuments-dist/.git/index.lock
	echo "\n\nautomatic-compile-cleanup killing everything\n\n" >> $(log-master-html)
	echo "\n\nautomatic-compile-cleanup killing everything\n\n" >> $(log-master-pdf)
	echo "\n\nautomatic-compile-cleanup killing everything\n\n" >> $(log-fall2017)

cleanup-repo:
	echo "\n\n Cleaning up the repo " >> $(log)
	df -h / >> $(log)
	git -C duckuments-dist show-ref -s HEAD > duckuments-dist/.git/shallow
	git -C duckuments-dist reflog expire --expire=0 --all
	git -C duckuments-dist prune
	git -C duckuments-dist prune-packed
	echo "\nafter cleanup\n" >> $(log)
	df -h / >> $(log)


automatic-compile-fall2017:
	git pull
	touch $(log-fall2017)
	echo "\n\n Starting" >> $(log-fall2017)
	date >> $(log-fall2017)
	-$(MAKE) fall2017
	echo "  succeded fall 2017" >> $(log-fall2017)
	-$(MAKE) upload
	echo "  succeded upload" >> $(log-fall2017)
	date >> $(log-fall2017)
	echo "Done." >> $(log-fall2017)


automatic-compile-master-html:
	#git pull
	touch $(log-master-html)
	echo "\n\nStarting" >> $(log-master-html)
	date >> $(log-master-html)
	nice -n 10 $(MAKE) master-html
	echo "  succeded html " >> $(log-master-html)
	nice -n 10 $(MAKE) master-split
	echo "  succeded split " >> $(log-master-html)
	date >>$(log-master-html)
	echo "Done." >> $(log-master-html)

automatic-compile-master-pdf:
	nice -n 10 $(MAKE) master-pdf
	echo "\n\nStarting" >> $(log-master-pdf)
	date >> $(log-master-pdf)
	echo "  succeded PDF  " >> $(log-master-pdf)
#	-$(MAKE) upload
	date >>  $(log-master-pdf)
	echo "Done." >> $(log-master-pdf)

automatic-compile-fall2017-pdf:
	echo "\n\nStarting" >> $(log-fall2017-pdf)
	date >> $(log-fall2017-pdf)
	nice -n 10 $(MAKE) fall2017-pdf
	echo "  succeded PDF  " >> $(log-fall2017-pdf)
	date >>  $(log-fall2017-pdf)
	echo "Done." >> $(log-fall2017-pdf)

upload:
	echo Not uploading


master-pdf: checks check-programs-pdf
	echo "This is now already implemented by make master"


update-mcdp:
	#
	# -git -C mcdp/ pull

update-software: checks
	-git -C $(duckietown-software) pull

compile:
	$(MAKE) master


index:
	mcdp-render -D misc book_index
	cp misc/book_index.html duckuments-dist/index.html



master: checks update-mcdp update-software
	DISABLE_CONTRACTS=1 mcdp-render-manual \
		--src $(src) \
		--stylesheet v_manual_split \
		--symbols $(tex-symbols) \
		-o out/master \
		--permalink_prefix http://purl.org/dth/ \
		--split       duckuments-dist/master/duckiebook/ \
		--pdf         duckuments-dist/master/duckiebook.pdf \
		--output_file duckuments-dist/master/duckiebook.html \
		-c "config echo 1; config colorize 1; rparmake"

master-clean:
	rm -rf out/master

books: \
	duckumentation \
	the_duckietown_project \
	opmanual_duckiebot_base \
	opmanual_duckiebot_fancy \
	opmanual_duckietown \
	software_carpentry \
	software_devel \
	software_architecture \
	class_fall2017 \
	class_fall2017_projects \
	learning_materials \
	exercises \
	code_docs \
	guide_for_instructors \
	deprecated

guide_for_instructors: checks update-mcdp update-software
	./run-book $@ docs/atoms_12_guide_for_instructors

deprecated: checks update-mcdp update-software
	./run-book $@ docs/atoms_98_deprecated

code_docs: checks update-mcdp update-software
	./run-book $@ duckietown/catkin_ws/src/

class_fall2017: checks update-mcdp update-software
	./run-book $@ docs/atoms_80_fall2017_info

learning_materials: checks update-mcdp update-software
	./run-book $@ docs/atoms_30_learning_materials

exercises: checks update-mcdp update-software
	./run-book $@ docs/atoms_40_exercises

duckumentation: checks update-mcdp update-software
	./run-book $@ docs/atoms_15_duckumentation

the_duckietown_project: checks update-mcdp update-software
	./run-book $@ docs/atoms_10_the_duckietown_project

opmanual_duckiebot_base: checks update-mcdp update-software
	./run-book $@ docs/atoms_17_setup_duckiebot_DB17-jwd

opmanual_duckiebot_fancy: checks update-mcdp update-software
	./run-book $@ docs/atoms_19_setup_duckiebot_DB17-wjdcl

opmanual_duckietown: checks update-mcdp update-software
	./run-book $@ docs/atoms_18_setup_duckietown

software_carpentry: checks update-mcdp update-software
	./run-book $@ docs/atoms_60_software_reference/12_software_carpentry

software_devel: checks update-mcdp update-software
	./run-book $@ docs/atoms_70_software_devel_guide

software_architecture: checks update-mcdp update-software
	./run-book $@ docs/atoms_80_duckietown_software

class_fall2017: checks update-mcdp update-software
	./run-book $@ docs/atoms_80_fall2017_info


class_fall2017_projects: checks update-mcdp update-software
	./run-book $@ docs/atoms_85_fall2017_projects

clean:
	rm -rf out

fall2017: checks update-mcdp update-software

	DISABLE_CONTRACTS=1 mcdp-render-manual \
		--src $(src) \
		--stylesheet v_manual_split \
		--no_resolve_references \
		--symbols $(tex-symbols) \
		--compose fall2017.version.yaml \
		-o out/fall2017\
		--output_file duckuments-dist/fall2017/duckiebook.html \
		--split duckuments-dist/fall2017/duckiebook/ \
		--pdf duckuments-dist/fall2017/duckiebook.pdf \
		 -c "config echo 1; rparmake"

fall2017-clean:
	rm -rf out/fall2017

duckuments-bot:
	python misc/slack_message.py

clean-tmp:
	find /mnt/tmp/mcdp_tmp_dir-duckietown -type d -ctime +10 -exec rm -rf {} \;

summaries:
	cp misc/frames.html duckuments-dist/index.html
	python -m mcdp_docs.summary_from_artefacts duckuments-dist duckuments-dist/summary.html

