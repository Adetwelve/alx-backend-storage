#!/usr/bin/env python3
import redis
r = redis.from_url('redis://foo.bar.com:12345')
r.ping()
