FROM postgres
LABEL maintainers="Mark Drilling <mdrillin@redhat.com>,Daniel Florian <dflorian@redhat.com>"
ENV POSTGRES_DB superset_demo
COPY initial_data.sql /docker-entrypoint-initdb.d/
