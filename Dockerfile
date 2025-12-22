FROM python:3.9-slim
WORKDIR /app
RUN pip install --no-cache-dir colorama
COPY christmas_tree.py .
CMD ["python", "christmas_tree.py"]