# Usar uma imagem base com suporte a GUI, como a do Ubuntu
FROM ubuntu:20.04
 
# Definir o fuso horário de forma não interativa
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
 
# Instalar dependências básicas
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \
    python3 python3-pip \
    x11vnc xvfb \
    fluxbox \
    wget \
    curl \
    supervisor \
    novnc \
    websockify \
    git \
    libgl1-mesa-glx
 
# Instalar Kivy e KivyMD
RUN pip3 install kivy
 
# Criar um diretório de trabalho
WORKDIR /src
 
# Copiar a aplicação para o container
COPY ./src /src
 
# Configurar o supervisor para gerenciar o VNC, noVNC e sua aplicação Python
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
 
# Expor as portas necessárias
EXPOSE 5900 7092
 
# Comando para iniciar o supervisor
CMD ["supervisord", "-n"]