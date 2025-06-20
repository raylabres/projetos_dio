# 💻 Desafios de Código - DIO

Este repositório armazena soluções para os desafios de código propostos pela [Digital Innovation One (DIO)](https://www.dio.me/), com o objetivo de praticar lógica de programação, estruturas de controle, manipulação de dados e outros conceitos fundamentais em diferentes linguagens.
## 📚 Sobre o Repositório
Os desafios aqui contidos foram realizados durante minha jornada de aprendizado com a DIO. Cada arquivo representa um problema resolvido, com o código correspondente e comentários quando necessário explicando a lógica por trás da solução.
## 🧠 Habilidades Desenvolvidas
- Lógica de Programação
- Estruturas Condicionais (if, else, match)
- Estruturas de Repetição (for, while)
- Entrada e Saída de Dados
- Manipulação de Strings e Números
- Criação e uso de Funções
- Dicionários, Listas, Tuplas
- Formatação de Dados (print(f"{variável:.2f}"), etc)
## 🛠 Tecnologias Utilizadas
- Python 🐍
## 📁 Estrutura do Projeto
📂 desafios-dio  
├── desconto_cupom.py  
├── outro_desafio.py  
├── README.md
## 🧪 Exemplo de Desafio Resolvido
🎯 Desafio: Aplicar Desconto com Cupom  
**Entrada:**  
100  
DESCONTO10  
**Saída:**  
90.00  
**Código:**  
```python
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}
preco = float(input())
cupom = input()
porcentagem_desconto = descontos[cupom]
preco_desconto = preco - (preco * porcentagem_desconto)
print(f"{preco_desconto:.2f}")
```
## 🚀 Como Executar
1. Certifique-se de ter o Python 3 instalado.  
2. Clone este repositório:  
```bash
git clone https://github.com/seu-usuario/desafios-dio.git
```  
3. Acesse o diretório e execute o desafio desejado:  
```bash
cd desafios-dio
python nome_do_arquivo.py
```
## 🤝 Contribuição
Contribuições são bem-vindas! Se quiser adicionar mais soluções, corrigir ou melhorar algo, sinta-se à vontade para abrir um Pull Request.
## 📜 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
## ✍️ Autor
Desenvolvido por **Ray Labres**  
