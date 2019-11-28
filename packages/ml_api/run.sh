#!/usr/bin/env bash
export IS_DEBUG=${DEBUG:-false}
exec gunicorn -b :${PORT:-5000} --access-logfile - --error-logfile - run:application

docker build --build-arg PIP_EXTRA_INDEX_URL=https://xNze1DjSe5zjdByuR4gr@pypi.fury.io/datainvestor/ -t ml_api:latest .
