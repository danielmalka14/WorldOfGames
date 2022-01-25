FROM python:3
RUN apt-get update -y
RUN pip install flask
WORKDIR /app
RUN mkdir templates
COPY ./alt_scores.html /app/templates
COPY ./game_scores.html /app/templates
COPY ./MainScores.py /app
COPY ./Scores.txt /app
COPY ./alt_score.txt /app
EXPOSE 80
CMD python /app/MainScores.py
