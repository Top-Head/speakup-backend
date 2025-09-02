# SpeakUp Backend

O **SpeakUp Backend** é uma API Flask para busca inteligente de artigos acadêmicos e citações, utilizando embeddings de linguagem natural para encontrar conteúdos relevantes em uma base local e, caso necessário, buscar online em fontes como [CORE](https://core.ac.uk/) e [Wikiquote](https://en.wikiquote.org/).

## Funcionalidades

- **Busca semântica**: Pesquisa documentos por similaridade de significado usando embeddings do modelo `all-MiniLM-L6-v2`.
- **Fontes automáticas**: Se não houver resultados relevantes localmente, busca artigos no CORE e citações no Wikiquote.
- **Armazenamento**: Salva documentos e embeddings em um banco SQLite.
- **API REST**: Endpoint `/api/search` para buscas via POST.

## Tecnologias

- Python 3.10+
- Flask
- Flask-SQLAlchemy
- Sentence Transformers
- SQLite

## Instalação

1. **Clone o repositório**
   ```sh
   git clone https://github.com/seu-usuario/speakup-backend.git
   cd speakup-backend
   ```

2. **Crie e ative um ambiente virtual**
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instale as dependências**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**
   - Renomeie `.env.example` para `.env` (ou edite o `.env` existente).
   - Insira sua chave da API do CORE:
     ```
     CORE_API_KEY=suachaveaqui
     ```

5. **Inicie o servidor**
   ```sh
   python server.py
   ```

## Uso

### Endpoint de busca

- **POST** `/api/search`
- **Body**:
  ```json
  {
    "query": "termo de busca"
  }
  ```
- **Resposta**:
  ```json
  [
    {
      "title": "Título",
      "url": "https://...",
      "text": "Trecho do texto...",
      "score": 0.87,
      "source": "CORE"
    }
  ]
  ```

Se não houver resultados relevantes, o backend busca automaticamente novos conteúdos online, armazena e retorna os resultados.

## Estrutura do Projeto

```
speakup-backend/
│
├── app/
│   ├── __init__.py         # Inicialização do Flask, DB e modelo
│   ├── models.py           # Definição do modelo Document
│   ├── routes.py           # Rotas da API
│   ├── service.py          # Integração com CORE e Wikiquote
│   └── utils.py            # Funções utilitárias (salvar documentos, chunking)
│
├── server.py               # Inicialização do servidor Flask
├── requirements.txt        # Dependências do projeto
├── .env                    # Variáveis de ambiente (não versionado)
└── README.md               # Este arquivo
```

## Licença

Este projeto está sob a licença MIT.

---

> **Dica:** Para uso em produção, configure variáveis sensíveis via ambiente e ajuste
