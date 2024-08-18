ARG PORT=443
FROM cypress/included:latest
RUN apt-get install python3 -y
RUN echo $(python3 -m site --user-base)
COPY requirements.txt .
ENV PATH /home/root/.local/bin: ${PATH}
RUN apt-get update && apt-get install -y python3-pip && pip install --break-system-packages -r requirements.txt
COPY . . 
CMD ["cypress", "run", "--no-sandbox"]
