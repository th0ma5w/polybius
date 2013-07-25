#!/bin/bash

export URL=http%253A%252F%252Ffeeds.kottke.org%252Fmain

curl http://127.0.0.1:3031/memrefresh/$URL > /dev/null;
