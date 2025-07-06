FROM python:3.11-slim

WORKDIR /app

COPY ../part1 /app

RUN pip install --no-cache-dir -r requirements.txt

# Ensure the shell script has executable permissions inside the image
COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]
