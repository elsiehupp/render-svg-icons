tests: test-basic test-files-with-unusual-filepaths
	@echo
	@echo "Success! All tests passed."
	@echo

test-basic:
	rm -f test/output.svg
	cp test/input.svg test/output.svg
	./svg-stroke-to-path SameStrokeColor 'stroke="#000"' test/output.svg

test-files-with-unusual-filepaths:
	rm -f test/output\ *.svg
	cp test/input.svg test/output\ 1.svg
	cp test/input.svg test/output\ 2.svg
	cp test/input.svg test/output\ 3.svg
	./svg-stroke-to-path SameStrokeColor \
		'stroke="#000"' \
		test/../test/output\ *.svg
