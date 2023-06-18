ARG os_name="alpine"
ARG os_version="3.18"
ARG repo="postgres"

FROM ${repo}:${os_name}${os_version}

COPY init.sql /docker-entrypoint-initdb.d/

