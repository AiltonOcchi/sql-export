# SQL Export - Exportador de Consultas SQL para CSV

Aplicação desktop com interface gráfica desenvolvida em Python que permite conectar-se a bancos de dados **PostgreSQL** ou **MySQL**, executar consultas SQL personalizadas e exportar os resultados para arquivos CSV de forma rápida e intuitiva.

## Características

- **Interface Gráfica Amigável**: Aplicação desktop completa desenvolvida com Tkinter
- **Suporte Multi-Banco**: Conecta-se tanto a PostgreSQL quanto MySQL
- **Teste de Conexão**: Valide suas credenciais antes de executar consultas
- **Editor SQL Integrado**: Área de texto com scroll para colar e editar consultas
- **Exportação Personalizável**: Escolha o nome e local de salvamento do arquivo CSV
- **Feedback em Tempo Real**: Barra de status mostrando progresso das operações
- **Validações Completas**: Sistema robusto de validação de campos e tratamento de erros
- **Codificação UTF-8**: Suporte completo para caracteres especiais e acentuação

## Funcionalidades

1. **Seleção de Banco de Dados**
   - Escolha entre PostgreSQL ou MySQL
   - Porta padrão ajustada automaticamente (5432 para PostgreSQL, 3306 para MySQL)

2. **Configuração de Conexão**
   - Host
   - Porta
   - Nome do banco de dados
   - Usuário
   - Senha (campo oculto)

3. **Teste de Conexão**
   - Valide credenciais antes de executar consultas
   - Feedback imediato de sucesso ou erro

4. **Execução de Consultas**
   - Editor SQL com scroll
   - Suporte a consultas complexas com múltiplos JOINs
   - Exibição de quantidade de registros retornados

5. **Exportação CSV**
   - Nome de arquivo personalizável
   - Seleção obrigatória de diretório de destino
   - Delimitador: ponto e vírgula (;)
   - Encoding: UTF-8
   - Cabeçalhos automáticos com nomes das colunas

## Requisitos

- **Python**: 3.6 ou superior (testado com Python 3.13.7)
- **Sistema Operacional**: Windows, Linux ou macOS
- **Banco de Dados**: PostgreSQL e/ou MySQL (servidor acessível)

## Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/sql-export.git
cd sql-export
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

**Dependências instaladas:**
- `psycopg2-binary>=2.9.10` - Driver PostgreSQL
- `mysql-connector-python>=8.0.0` - Driver MySQL

## Como Usar

### Execução via Python

```bash
python sql_export.py
```

### Execução via Executável (Windows)

1. Gere o executável usando o script fornecido:
```bash
gerar_executavel.bat
```

2. O executável estará disponível em: `dist\ExportadorPostgreSQL.exe`

3. Execute o arquivo `.exe` diretamente (não requer Python instalado)

## Fluxo de Uso

1. **Selecione o tipo de banco de dados** (PostgreSQL ou MySQL)
2. **Preencha os dados de conexão**:
   - Host (ex: localhost)
   - Porta (ajustada automaticamente)
   - Nome do banco
   - Usuário e senha
3. **Teste a conexão** usando o botão "Testar Conexão"
4. **Cole sua consulta SQL** na área de texto
5. **Defina o nome do arquivo** CSV (extensão .csv é adicionada automaticamente)
6. **Selecione o local** onde deseja salvar o arquivo (obrigatório)
7. **Clique em "Exportar para CSV"**
8. **Aguarde a confirmação** com quantidade de registros exportados

## Estrutura do Projeto

```
sql-export/
├── sql_export.py           # Aplicação principal com interface gráfica
├── requirements.txt        # Dependências do projeto
├── gerar_executavel.bat   # Script para gerar executável Windows
└── README.md              # Documentação do projeto
```

## Gerando Executável

Para distribuir a aplicação sem necessidade de Python instalado:

### Windows
Execute o arquivo `gerar_executavel.bat` que automatiza:
- Instalação do PyInstaller
- Geração do executável único
- Limpeza de arquivos temporários

Ou manualmente:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "ExportadorSQL" sql_export.py
```

### Linux/macOS
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "ExportadorSQL" sql_export.py
```

## Exemplo de Uso

### Consulta Simples
```sql
SELECT * FROM usuarios WHERE ativo = true
```

### Consulta com JOINs
```sql
SELECT 
    u.nome,
    u.email,
    p.titulo as cargo,
    d.nome as departamento
FROM usuarios u
INNER JOIN cargos p ON u.id_cargo = p.id
INNER JOIN departamentos d ON u.id_departamento = d.id
WHERE u.data_admissao >= '2024-01-01'
```

## Configurações do CSV

- **Delimitador**: Ponto e vírgula (`;`)
- **Encoding**: UTF-8
- **Quebra de linha**: Automática
- **Cabeçalho**: Primeira linha contém os nomes das colunas

## Tratamento de Erros

A aplicação possui validações para:
- Campos obrigatórios vazios
- Falhas de conexão ao banco de dados
- Erros na execução de consultas SQL
- Problemas na criação/gravação de arquivos
- Consultas sem resultados

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abrir um Pull Request

## Autor

**Ailton Occhi**

- GitHub: [@AiltonOcchi](https://github.com/AiltonOcchi)

## Agradecimentos

- Interface gráfica desenvolvida com [Tkinter](https://docs.python.org/3/library/tkinter.html)
- Conexão PostgreSQL via [psycopg2](https://www.psycopg.org/)
- Conexão MySQL via [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)

---

Se este projeto foi útil para você, considere dar uma estrela no GitHub!
