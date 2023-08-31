# Install project dependencies
install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt


# Format code using Black
format:
	find . -name "*.py" | xargs black

# Run pylint on all Python files
lint:
	find . -name "*.py" | xargs pylint

.PHONY: install format lint

# Run tests using unittest
test:
	python -m unittest discover tests

# Run all code quality checks
quality: format lint

# Run the Flask app
run:
	python app.py