ARG os_name="alpine"
ARG os_version="3.18"
ARG py_version="3.11"
ARG repo="python"

FROM ${repo}:${py_version}-${os_name}${os_version}

RUN adduser \
    --disabled-password \
    user

WORKDIR /Code

COPY --chown=user:user . .

RUN chmod +x /Code/entrypoint.sh

RUN pip3 install --upgrade --upgrade pip && \
    pip3 install -r requirements.txt && \
    rm requirements.txt

USER user

WORKDIR /Code

CMD ["./entrypoint.sh"]