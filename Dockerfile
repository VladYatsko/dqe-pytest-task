FROM jenkins/jenkins:latest
USER root
WORKDIR /app
COPY . .
RUN apt-get update
RUN apt-get install -y python3-pip unixodbc-dev
RUN apt-get install -y freetds-dev tdsodbc && \
    echo "[sqlserver]" >> /etc/odbc.ini && \
    echo "Description = SQL Server" >> /etc/odbc.ini && \
    echo "Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so" >> /etc/odbc.ini && \
    echo "Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" >> /etc/odbc.ini && \
    echo "Server = EPBYBREW00A1\SQLEXPRESS" >> /etc/odbc.ini