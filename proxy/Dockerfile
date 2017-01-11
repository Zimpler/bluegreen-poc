FROM nginx:1.11.8

# RUN apt-get update
# RUN apt-get install -y software-properties-common
# RUN add-apt-repository ppa:vbernat/haproxy-1.7
# RUN apt-get update
# RUN apt-get install -y haproxy

RUN rm /etc/nginx/conf.d/default.conf

RUN echo 'exit 0' > /usr/sbin/policy-rc.d

RUN echo '#!/bin/bash\n/etc/init.d/nginx start && tail -f /var/log/nginx/*.log' > /bin/run_nginx

RUN chmod +x /bin/run_nginx
