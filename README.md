

# Gerenciamento de Igrejas

![Badge de Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

## Índice

- [Descrição do Projeto](#descrição-do-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Autores](#autores)

## Descrição do Projeto

O **Gerenciamento de Igrejas** é uma aplicação web desenvolvida para auxiliar igrejas na administração de seus membros e transações financeiras. O sistema oferece uma interface intuitiva para gerenciar informações de membros, departamentos, fornecedores, documentos fiscais e tipos de trabalhadores, além de facilitar o controle de transações financeiras e documentos fiscais.

## Funcionalidades

- **Gerenciamento de Usuários Personalizados (customuser):** Controle de autenticação e autorização com perfis de usuário personalizados.
- **Departamentos (department):** Criação e administração de departamentos dentro da igreja.
- **Membros do Departamento (department_member):** Associação de membros a departamentos específicos.
- **Transações Financeiras (fiscal_transaction):** Registro e acompanhamento de entradas e saídas financeiras.
- **Membros (member):** Cadastro e gerenciamento de informações pessoais e de contato dos membros da igreja.
- **Fornecedores (suppliers):** Cadastro e controle de fornecedores de serviços e produtos.
- **Documentos Fiscais (tax_document):** Emissão e armazenamento de notas fiscais e outros documentos relacionados.
- **Locações (tenancy):** Gestão de contratos de locação e uso de espaços da igreja.
- **Tipos de Trabalhadores (worker_type):** Definição e categorização dos diferentes tipos de colaboradores e voluntários.

## Tecnologias Utilizadas

- **Linguagem:** Python
- **Framework Web:** Django
- **Banco de Dados:** PostgreSQL

## Instalação

Para executar este projeto localmente, siga os passos abaixo:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/gerenciamento-de-igrejas.git
   ```

2. **Acesse o diretório do projeto:**

   ```bash
   cd gerenciamento-de-igrejas
   ```

3. **Crie um ambiente virtual:**

   ```bash
   python3 -m venv venv
   ```

4. **Ative o ambiente virtual:**

   - No Windows:

     ```bash
     venv\Scripts\activate
     ```

   - No Unix/MacOS:

     ```bash
     source venv/bin/activate
     ```

5. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

6. **Configure o banco de dados:**

   Certifique-se de que o PostgreSQL esteja instalado e em execução. Crie um banco de dados para o projeto e atualize as configurações no arquivo `settings.py`.

7. **Aplique as migrações:**

   ```bash
   python manage.py migrate
   ```

8. **Crie um superusuário (opcional):**

   ```bash
   python manage.py createsuperuser
   ```

9. **Inicie o servidor de desenvolvimento:**

   ```bash
   python manage.py runserver
   ```

## Uso

Após iniciar o servidor, acesse `http://localhost:8000/` em seu navegador para utilizar a aplicação. Utilize as credenciais do superusuário para acessar o painel administrativo e gerenciar as diferentes funcionalidades do sistema.

## Contribuição

Contribuições são bem-vindas! Se você deseja colaborar com este projeto, siga os passos abaixo:

1. **Faça um fork deste repositório.**
2. **Crie uma branch para sua feature:**

   ```bash
   git checkout -b minha-nova-feature
   ```

3. **Faça commit das suas alterações:**

   ```bash
   git commit -m 'Adiciona nova funcionalidade'
   ```

4. **Envie para a branch principal:**

   ```bash
   git push origin minha-nova-feature
   ```

5. **Abra um Pull Request.**

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.

## Autor

- **João Vitor Guchert Eggers:** [joaoguchert195@gmail.com](mailto:joaoguchert195@gmail.com)
