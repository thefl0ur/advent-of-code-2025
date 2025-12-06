.ONESHELL:

number = $(error Day number is required! Use make gen number=x)

all: gen

gen:
	@mkdir aoc/day${number}
	@touch aoc/day${number}/input.md
	@touch aoc/day${number}/test_input.md
	@cat .templates/__init__.py > aoc/day${number}/__init__.py
	@cat .templates/__main__.py > aoc/day${number}/__main__.py
	@cat .templates/solution.py > aoc/day${number}/solution.py
	@sed \
		-e "s|{{NUMBER}}|$(number)|g" \
		.templates/test_day.tpl > tests/test_day$(number).py
	@echo "Initialized"