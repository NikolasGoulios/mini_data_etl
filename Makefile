.PHONY: help clean run drop show_drop install

help:
	@echo "Usage: make <target>"
	@echo "Targets:"
	@echo "  run - Run the clean script"
	@echo "  drop - Run the drop script"
	@echo "  clean - Clean the data"
	@echo "  drop - Drop the data"
	@echo "  show_drop - Show the dropped rows"
	@echo "  install - Install the requirements"

run:
	python3 Csv_Cleaner/scripts/clean.py

drop:
	python3 Csv_Cleaner/scripts/dropped.py

clean:
	rm -rf Csv_Cleaner/data/clean/*.csv
	rm -rf Csv_Cleaner/data/dropped/*.csv

show_drop:
	@echo "Dropped rows:"
	@cat Csv_Cleaner/data/dropped/*.csv | wc -l

install:
	pip install -r Csv_Cleaner/requirements.txt
