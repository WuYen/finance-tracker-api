# Run the FastAPI server
run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Install dependencies
install:
	pip install -r requirements.txt

# Format code
format:
	black .

# Run tests
test:
	pytest
