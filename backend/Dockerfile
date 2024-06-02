FROM python:3.12.3-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . /app/

# Install torch and torchvision CPU only versions
RUN pip3 install torch==2.2.2+cpu torchvision==0.17.2+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html

# Explicitly install ultralytics without optional dependencies (like CUDA).
RUN pip3 install ultralytics==8.2.27 --no-deps

# Install the rest of the packages
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# OS libs for psql
RUN apt-get update && apt-get install -y libpq-dev ffmpeg libsm6 libxext6

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"] 