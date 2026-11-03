.PHONY: run help check clean

# Start MiniOS Web Terminal
run:
	python app.py

# Display available commands
help:
	@echo "MiniOS Makefile Commands:"
	@echo "make run   - Start MiniOS Web Terminal"
	@echo "make check - Check Python files"
	@echo "make clean - Remove Python cache files"

# Check Python files for syntax errors
check:
	python -m compileall -q .

# Remove Python cache
clean:
	powershell -Command "Get-ChildItem -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force"
