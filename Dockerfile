FROM python

RUN pip install pytest

RUN mkdir files

ADD conftest.py /files
ADD data.py /files
ADD test_example.py /files

WORKDIR /files

CMD ["py.test", "-s", "-v","test_example.py"]
