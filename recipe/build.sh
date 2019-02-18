#!/bin/sh

export LDFLAGS="$LDFLAGS -shared"

python setup.py install --single-version-externally-managed --record=record.txt