# Proof for Concept for blue-green deploys with docker

What it does:

blue-green deploy an HTTP app that takes 10s to boot. Zero downtime, zero slowdowns.

Dependencies:
- ansible
- docker
- ab (if you want to load test)

To run benchmark:

```
ab -l -n 100000 http://bluegreen.dev:8080/
```

Then run a bunch of deploy:

```
ansible-playbook deploy.yml
```

Making sure the deployed version alternates between blue and green.

Result:

It works! zero failed request, zero slow-down.

```
Server Software:        nginx/1.11.8
Server Hostname:        bluegreen.dev
Server Port:            8080

Document Path:          /
Document Length:        Variable

Concurrency Level:      1
Time taken for tests:   174.236 seconds
Complete requests:      100000
Failed requests:        0
Total transferred:      15553111 bytes
HTML transferred:       3353111 bytes
Requests per second:    573.94 [#/sec] (mean)
Time per request:       1.742 [ms] (mean)
Time per request:       1.742 [ms] (mean, across all concurrent requests)
Transfer rate:          87.17 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   1.8      0     137
Processing:     1    1   1.3      1     153
Waiting:        0    1   1.2      1     153
Total:          1    2   2.2      1     154

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      1
  75%      2
  80%      2
  90%      2
  95%      3
  98%      5
  99%      6
  100%    154 (longest request)
```
