# Install project dependencies
install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt


# Format code using Black
format:
	black .*py

# Run pylint on all Python files
lint:
	find . -name "*.py" | xargs pylint

.PHONY: install format lint

# Run all code quality checks
quality: format lint