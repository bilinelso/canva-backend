#!/bin/bash

# Cria pastas se não existirem
mkdir -p fonts
mkdir -p template

# Baixa a imagem do template
wget -O template/template.png "https://files.chatboxcdn.com/file-DZDWjgnozfphvL9pz3ejz4"

# Baixa as fontes nas pastas corretas
wget -O fonts/OpenSans-Light.ttf "https://files.chatboxcdn.com/file-SxRg3AVYpkMBuDXWGjg3vQ"
wget -O fonts/OpenSans-Medium.ttf "https://files.chatboxcdn.com/file-DVXJXXi5wvgDf3ikftMznh"
wget -O fonts/OpenSans-Bold.ttf "https://files.chatboxcdn.com/file-9jRqXPqUuHDUvFEEatvbJZ"
wget -O fonts/OpenSans-SemiBold.ttf "https://files.chatboxcdn.com/file-BMxo6LdMCp8cqRxRxueQ9h"
