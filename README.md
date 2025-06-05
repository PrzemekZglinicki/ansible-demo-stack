# ansible-demo-stack

## About

Ansible example usage. The project contains docker based setup for the ansible lab - 5 actors contains loadbalancer, webserver hosts, database and control host. Project crated for learing purpose.

## Prerequisites
1. **Install Docker**
2. **Install Ansible**

## Usage

Create ssh-key to connect from ansible to docker hosts. I am using id_ed25519 key.

To build and run docker containters:
```bash
cd docker && docker compose build --build-arg SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)" && docker compose up -d && cd -
```

To check whether docker containers starts correctly:
```bash
docker ps
```

To set up infrastructure run:
```bash
cd ansible && ansible-playbook site.yml
```

To check if everythink works and has connections to each other:
```bash
ansible-playbook playbooks/stack_status.yml
```


# ansible-demo-stack

## About

This project demonstrates an example setup using **Ansible** to manage a **Docker-based lab environment**.
It includes 5 containers acting as different infrastructure components:

- `control`: the Ansible control node
- `lb01`: load balancer (nginx)
- `app01` & `app02`: webserver hosts (Flask app)
- `db01`: MySQL database server

The project is intended for **learning and experimenting with Ansible** in a simulated multi-host environment.

---

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) (with Docker Compose)
- [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
- SSH key pair (I use `id_ed25519`)

---

## Usage

### 🔐 1. Generate an SSH key (if not done already)

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519
```

This key will allow the control container to connect to the other containers via SSH.

---

### 🐳 2. Build and run Docker containers

```bash
cd docker
docker compose build --build-arg SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
docker compose up -d
cd -
```

---

### ✅ 3. Check if containers are running

```bash
docker ps
```

You should see all 5 containers: `control`, `lb01`, `app01`, `app02`, and `db01`.

---

### ⚙️ 4. Provision the infrastructure using Ansible

```bash
cd ansible
ansible-playbook site.yml
```

This will install packages, deploy services, and configure your environment.

---

### 🔍 5. Verify the stack status and connectivity

```bash
ansible-playbook playbooks/stack_status.yml
```

This playbook checks that the services are up and reachable from the Ansible control host.

---

## Notes

- Each container runs SSH on a unique port, exposed to the host
- The control node uses the SSH key you provide to connect to others
- The setup is great for learning Ansible roles, handlers, templates, inventories, and more

---

## 🔐 SSH Shortcuts (optional)

You can optionally configure SSH aliases to make it easier to access your Docker hosts:

### Example `~/.ssh/config`:

```ssh-config
Host control
  HostName 127.0.0.1
  Port 2200
  User ansible
  IdentityFile ~/.ssh/id_ed25519
  StrictHostKeyChecking no
  UserKnownHostsFile=/dev/null

Host lb01
  HostName 127.0.0.1
  Port 2201
  User ansible
  IdentityFile ~/.ssh/id_ed25519
  StrictHostKeyChecking no
  UserKnownHostsFile=/dev/null

... (others omitted for brevity)
```

Save this configuration as `~/.ssh/config`, or use the provided template:

```bash
cp ssh/ssh_config.example ~/.ssh/config
```

Now you can SSH into your containers with short aliases:

```bash
ssh control
ssh app01
```

> 🛡️ **Security Note**: `StrictHostKeyChecking no` and `UserKnownHostsFile=/dev/null` make SSH connections easier in local dev environments, but should **not** be used in production setups.
