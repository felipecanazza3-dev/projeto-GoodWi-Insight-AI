# GoodWi Insight AI - Sistema Integrado de Monitorização Solar e Assistência Técnica

Sistema Web desenvolvido na plataforma Django para processamento de telemetria fotovoltaica em tempo real, gestão de unidades consumidoras e integração de assistente generativo via API LLM com restrição de contexto.

---

## Integrantes do Projeto

* Felipe Alves Canazza
* Eduardo Oliveira Reis
* Pedro Andreaza
* caio ceschini

---

## Arquitetura de Software e Fluxo de Dados

A aplicação adota o padrão MVT (Model-View-Template) do Django, integrando rotas assíncronas para comunicação via JSON (AJAX/Fetch API) e serviços externos de inteligência artificial.

### Componentes do Sistema

1. **Core Backend:** Django Framework com rotas estruturadas em `views.py`.
2. **Persistência de Dados:** SQLite3 gerido via Django ORM.
   - `Metric`: Armazena telemetria instantânea (consumo, geração solar e custo).
   - `ConsumerUnit`: Armazena parâmetros da instalação (modelo do inversor, potência nominal `kWp` e tarifa `R$/kWh`).
3. **Módulo de IA:** Biblioteca `google.generativeai` parametrizada com o modelo `gemini-2.5-flash` e instruções de sistema ativas.
4. **Interface de Utilizador:** Templates HTML5 responsivos (`grafico.html`, `ia.html`, `perfil.html`, `home.html`) integrando bibliotecas JavaScript para renderização de gráficos em tempo real.

---

## Detalhamento Técnico das Implementações

### 1. Ingestão e Processamento de Telemetria (`get_live_data`)
A rota gera dados pontuais de consumo (`kWh`), geração fotovoltaica e calcula o custo estimado correspondente. Cada leitura é gravada na base de dados através da classe `Metric` e devolvida em formato `JsonResponse` para atualização do dashboard cliente.

### 2. Integração com LLM e Restrição de Contexto (`ask_gemini`)
O endpoint processa requisições HTTP POST contendo o prompt do utilizador. Utiliza a SDK oficial do Google Gemini configurada via variável de ambiente `GEMINI_API_KEY`.
- **Modelo utilizado:** `gemini-2.5-flash`.
- **System Instruction:** Injeção de regras no construtor `genai.GenerativeModel`, limitando o âmbito de atuação do modelo estritamente a produtos GoodWe (inversores, baterias) e métricas do sistema.

### 3. Gestão da Unidade Consumidora (`perfil`)
Executa a persistência de estado através do método `get_or_create` do ORM na tabela `ConsumerUnit`. Atualiza campos de configuração como `inverter_model`, `system_power_kwp` e `energy_tariff_brl`.

---

## Configuração do Ambiente e Execução

### Pré-requisitos
* Python 3.10 ou superior
* Gestor de pacotes `pip`

### Instruções de Instalação

1### Instruções de Instalação e Execução

1. **Criar e ativar o ambiente virtual:**

   * **Windows:**
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```

   * **Linux/macOS:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

2. **Instalar as dependências do projeto:**
   ```bash
   pip install django google-generativeai python-dotenv

3. **Configurar as variáveis de ambiente:**
```bash
Crie um ficheiro .env na raiz do projeto com a seguinte chave:

Snippet de código
GEMINI_API_KEY=sua_chave_api_aqui
```

4. **Executar as migrações da base de dados:**
 ```bash
python manage.py makemigrations
python manage.py migrate
```
5. **Iniciar o servidor de desenvolvimento:**
```bash
python manage.py runserver
```
