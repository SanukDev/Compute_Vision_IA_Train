1. 📌 Visão Geral do Projeto
Este projeto tem como objetivo desenvolver um sistema de reconhecimento de gestos da Língua Brasileira de Sinais (Libras) utilizando técnicas de visão computacional e aprendizado de máquina, sem dependência de bibliotecas avançadas como MediaPipe.
O sistema captura imagens da câmera, processa os dados visuais e classifica gestos pré-definidos, como “OI”, “SIM” e “NÃO”.
2. 🎯 Objetivo
Objetivo Geral
Desenvolver um sistema capaz de reconhecer gestos de Libras em tempo real utilizando técnicas de inteligência artificial baseadas em imagens.
Objetivos Específicos
Capturar imagens da mão através da webcam
Pré-processar imagens (redimensionamento e escala de cinza)
Criar um dataset de gestos rotulados
Treinar um modelo de Machine Learning
Realizar reconhecimento de gestos em tempo real
3. 🧠 Tecnologias Utilizadas
Python 3
OpenCV → captura e processamento de imagem
NumPy → manipulação de dados
Scikit-learn → modelo de Machine Learning
Joblib → salvamento do modelo treinado
4. ⚙️ Arquitetura do Sistema
O sistema segue o seguinte fluxo:
Câmera (Webcam)
      ↓
Captura de imagem (OpenCV)
      ↓
Recorte da região de interesse (ROI)
      ↓
Pré-processamento (64x64 grayscale)
      ↓
Conversão para vetor
      ↓
Modelo de Machine Learning (RandomForest)
      ↓
Predição do gesto
      ↓
Exibição do resultado na tela
5. 📂 Estrutura do Projeto
libras-ia/
│
├── dataset/
│   ├── OI/
│   ├── SIM/
│   └── NAO/
│
├── collect.py
├── train.py
├── detect.py
└── libras.pkl
6. 📸 Coleta de Dados
🔧 Funcionamento
O sistema captura imagens da webcam e permite salvar amostras de gestos manualmente.
Código principal (resumo funcional):
Captura vídeo em tempo real
Define uma região central da imagem (ROI)
Salva imagens quando o usuário pressiona a tecla S
Organiza imagens por classe (label)
Entrada:
Imagem da webcam
Saída:
Dataset organizado em pastas por gesto
7. 🧹 Pré-processamento
Cada imagem passa por:
Redimensionamento para 64x64 pixels
Conversão para escala de cinza
Transformação em vetor (flatten)
Isso reduz a complexidade e facilita o aprendizado do modelo.
8. 🧠 Treinamento do Modelo
Algoritmo utilizado:
Random Forest Classifier
Processo:
Carregamento das imagens do dataset
Transformação em vetores numéricos
Associação com labels (classes)
Treinamento do modelo
Salvamento do modelo com Joblib
Saída:
Arquivo: libras.pkl
9. 🖐️ Reconhecimento em Tempo Real
Funcionamento:
Captura vídeo da webcam
Aplica o mesmo pré-processamento do treino
Envia dados para o modelo
Recebe a previsão do gesto
Exibe o resultado na tela
Resultado:
O sistema mostra na tela o gesto identificado em tempo real.
10. 📊 Modelo de Machine Learning
Tipo de modelo:
Aprendizado supervisionado
Algoritmo:
Random Forest
Entrada:
Vetor de pixels da imagem (64x64 = 4096 valores)
Saída:
Classe do gesto (ex: OI, SIM, NAO)
11. ⚠️ Limitações do Sistema
Sensível à iluminação
Dependente de fundo relativamente limpo
Menor precisão em comparação com modelos baseados em deep learning
Não reconhece Libras completa (apenas gestos isolados)
12. 🚀 Possíveis Melhorias
Substituir Random Forest por CNN (Redes Neurais Convolucionais)
Melhorar segmentação da mão (remoção de fundo)
Aumentar dataset com mais variações
Implementar reconhecimento de frases completas
Adicionar tradução para voz
13. 📌 Conclusão
O sistema demonstra que é possível construir um reconhecedor de gestos de Libras funcional sem MediaPipe, utilizando apenas técnicas clássicas de visão computacional e aprendizado de máquina.
Apesar de suas limitações, o projeto é eficiente como protótipo educacional e base para sistemas mais avançados de acessibilidade digital.