# Command
```
ab -n 10000 -c 50 http://localhost:8800/api/v1/grands-prix
```
(!) Remove decorator @check_token before running



# w/ balancing

```
This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 1000 requests
Completed 2000 requests
Completed 3000 requests
Completed 4000 requests
Completed 5000 requests
Completed 6000 requests
Completed 7000 requests
Completed 8000 requests
Completed 9000 requests
Completed 10000 requests
Finished 10000 requests


Server Software:        
Server Hostname:        localhost
Server Port:            8800

Document Path:          /api/v1/grands-prix
Document Length:        773 bytes

Concurrency Level:      50
Time taken for tests:   13.358 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      9330000 bytes
HTML transferred:       7730000 bytes
Requests per second:    748.59 [#/sec] (mean)
Time per request:       66.792 [ms] (mean)
Time per request:       1.336 [ms] (mean, across all concurrent requests)
Transfer rate:          682.06 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0       3
Processing:     2   66  64.9     81     212
Waiting:        2   66  64.9     81     211
Total:          2   67  64.9     83     212

Percentage of the requests served within a certain time (ms)
  50%     83
  66%    111
  75%    130
  80%    135
  90%    145
  95%    163
  98%    176
  99%    183
 100%    212 (longest request)
```

# w/out balancing
```
This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 1000 requests
Completed 2000 requests
Completed 3000 requests
Completed 4000 requests
Completed 5000 requests
Completed 6000 requests
Completed 7000 requests
Completed 8000 requests
Completed 9000 requests
Completed 10000 requests
Finished 10000 requests


Server Software:        
Server Hostname:        localhost
Server Port:            8800

Document Path:          /api/v1/grands-prix
Document Length:        773 bytes

Concurrency Level:      50
Time taken for tests:   21.441 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      9330000 bytes
HTML transferred:       7730000 bytes
Requests per second:    466.39 [#/sec] (mean)
Time per request:       107.206 [ms] (mean)
Time per request:       2.144 [ms] (mean, across all concurrent requests)
Transfer rate:          424.95 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       3
Processing:     7  107  18.8    101     188
Waiting:        7  107  18.8    101     188
Total:          9  107  18.8    101     188

Percentage of the requests served within a certain time (ms)
  50%    101
  66%    112
  75%    119
  80%    123
  90%    133
  95%    144
  98%    154
  99%    164
 100%    188 (longest request)
 ```
