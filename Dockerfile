# this one has python 3.13, which gives problems with gensim
# FROM quay.io/jupyter/pytorch-notebook:cuda12-2025-09-08
# this one is most recent python 3.12 version
# and is the sha for what should be version cuda12-python-3.12
FROM quay.io/jupyter/pytorch-notebook@sha256:62e5c27a27e8eaa08d044c920a40061f4d3763d02a7bc56d40e689a878d07c65 

COPY requirements_min.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
