FROM ubuntu:22.04

ARG SSH_PUB_KEY

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-distutils \
    python3-venv \
    openssh-server \
    sudo \
    locales \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8
ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8

# Add ansible user with sudo privileges
RUN useradd -ms /bin/bash ansible && \
    echo "ansible ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# SSH setup for root and ansible user
COPY ssh_config /root/.ssh/config

RUN mkdir /var/run/sshd && \
    mkdir -p /root/.ssh /home/ansible/.ssh && \
    chmod 700 /root/.ssh /home/ansible/.ssh && \
    echo "$SSH_PUB_KEY" > /root/.ssh/authorized_keys && \
    echo "$SSH_PUB_KEY" > /home/ansible/.ssh/authorized_keys && \
    chmod 600 /root/.ssh/authorized_keys /home/ansible/.ssh/authorized_keys && \
    chown ansible:ansible /home/ansible/.ssh -R

# Minimal system services cleanup
RUN /usr/sbin/update-rc.d -f ondemand remove && \
  for f in /etc/init/u*.conf /etc/init/mounted-*.conf /etc/init/hostname.conf \
           /etc/init/networking.conf /etc/init/tty*.conf /etc/init/plymouth*.conf \
           /etc/init/hwclock*.conf /etc/init/module*.conf; do \
    dpkg-divert --local --rename --add "$f"; \
  done && \
  echo '# /lib/init/fstab: cleared out for bare-bones Docker' > /lib/init/fstab

ENV container docker

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
