ARG VARIANT=3
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

ENV PYTHONUNBUFFERED 1

# Update args in docker-compose.yaml to set the UID/GID of the "vscode" user.
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG USERNAME=vscode
RUN if [ "$USER_GID" != "1000" ] || [ "$USER_UID" != "1000" ]; then groupmod --gid $USER_GID vscode && usermod --uid $USER_UID --gid $USER_GID vscode; fi

# [Option] Install Node.js
ARG INSTALL_NODE="false"
ARG NODE_VERSION="lts/*"
RUN if [ "${INSTALL_NODE}" = "true" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

# Install kubectl
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl && \
    chmod +x ./kubectl && \
    mv ./kubectl /usr/local/bin/kubectl && \
    kubectl version --client

# Install helm
RUN curl -fsSL -o - https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash && \
    helm version

# Install sops
RUN wget -nv -O /usr/bin/sops https://github.com/mozilla/sops/releases/download/v3.7.2/sops-v3.7.2.linux.amd64 && \
    chmod +x /usr/bin/sops

# Install postgresql client
RUN apt update && \
    apt install -y postgresql-client

# Create vscode extensions directory
RUN mkdir -p /home/$USERNAME/.vscode-server/extensions && \
    chown -R $USERNAME /home/$USERNAME/.vscode-server

# Install poetry
RUN pip install poetry

USER vscode

# Setup poetry
RUN poetry config virtualenvs.in-project true

# Install helm-secrets
RUN helm plugin install https://github.com/jkroepke/helm-secrets --version v3.12.0
