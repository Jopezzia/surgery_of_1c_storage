FROM python:3.8.10-slim-buster
WORKDIR /opt/surgery_of_1c_storage
COPY starter ./
COPY lib_linux/click ./lib_linux/click
COPY lib_linux/click-7.1.2.dist-info ./lib_linux/click-7.1.2.dist-info
COPY lib_linux/pyodbc.py ./lib_linux/pyodbc.py
COPY surgery_of_1c_storage ./surgery_of_1c_storage
COPY requirements_linux.txt ./
RUN pip install -r requirements_linux.txt
CMD ./starter init-config -n config.ini && ./starter add-admin
