# Install project dependencies
install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt


# Format code using Black
format:
	black .*py

