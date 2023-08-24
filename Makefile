# Install project dependencies
install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

# Create and activate virtual environment
venv:
	$(PYTHON) -m venv $(VENV_NAME)
	source $(VENV_ACTIVATE)

# Run the Flask development server
run:
	$(PYTHON) app.py