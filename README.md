# Dublefy
A motivação para a criação desse projeto foi um caso pessoal, onde dupliquei várias músicas em minha playlist do Spotify. Pela quantidade de duplicatas, a melhor solução foi criar esse projeto. 
## Pré-requisitos

- Back-end >
  `Python 3.12.*` | `Poetry`
- Front-end > `pnpm`

## Preparar ambientes

```bash
# Entrar no diretório back-end
cd back-end

# Criar ambiente virtual e instalar pacotes
poetry install

# Ativar ambiente virtual
poetry shell

# Para iniciar a API
task run
```

```bash
# Entrar no diretório front-end
cd front-end

# Instalar pacotes
pnpm install

# Para iniciar o front
pnpm vite
```

## Informações adicionais

Para mais comandos com o uso do `task` consulte o arquivo `pyproject.toml` no diretório back-end na sessão `[tool.taskipy.tasks]`.

Outros detalhes do uso e instalação do [`pnpm`](https://pnpm.io/motivation)
e [`poetry`](https://python-poetry.org/docs/), consulte a documentação oficial.
