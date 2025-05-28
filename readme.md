🖐️ Detector de Gesto de Socorro – Blackout Guardian
📌 Descrição do Problema
A falta de energia elétrica é um desafio frequente no Brasil, afetando tanto áreas urbanas quanto rurais. Eventos extremos, como tempestades e alagamentos, causam interrupções no fornecimento de energia, comprometendo semáforos, transportes e serviços essenciais. A fragilidade da infraestrutura elétrica frente a desastres naturais exige soluções rápidas, acessíveis e eficazes. Além disso, a ausência de um sistema centralizado para relatar e responder a essas falhas intensifica os impactos para cidadãos e provedores de serviço.

💡 Visão Geral da Solução
Desenvolvemos uma solução simples e funcional que permite a detecção de um gesto de socorro com a mão, mesmo em ambientes com pouca ou nenhuma iluminação, utilizando Python e MediaPipe.

✅ Objetivos:
Permitir que pessoas em situação de risco solicitem ajuda com um gesto.

Não depender de hardware adicional como ESP32 ou Arduino.

Funcionar com webcam comum e em ambientes de baixa luz.

Ser uma solução leve, prática e fácil de usar ou integrar a outros sistemas.

🧠 Tecnologias Utilizadas
Python 3.x

MediaPipe (Google)

OpenCV

Webcam comum (pode ser integrada ou USB)

🔧 Como Funciona
O sistema reconhece o seguinte gesto de socorro:

Polegar dobrado para dentro

Demais dedos (indicador ao mínimo) abaixados

Esse gesto é similar ao gesto de “violência doméstica” amplamente divulgado em campanhas de apoio.

Quando detectado, o sistema exibe uma mensagem de alerta na tela:
    SINAL DE PEDIDO DE AJUDA DETECTADO ⚠

▶️ Como Executar o Projeto
clone o repositorio: https://github.com/LoGoMax1/GS-IOT

📹 Vídeo Demonstrativo
https://www.youtube.com/watch?v=MRJVS_lCKpA&ab_channel=LorenzoGomes


👥 Integrantes do Grupo

| Nome                     | RM      |
| Lorenzo Gomes Andreata   | RM551117|
| Henri De Oliveira Lopes  | RM98347 |
