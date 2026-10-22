# ⚡ GoodWi AI — Solução Integrada de Gestão Energética & Mobilidade Elétrica GoodWe

> **Sprint 4 — Solução Final Integrada e Inovadora**  

---

## 📌 1. Visão Geral do Projeto

O **GoodWi AI** é uma plataforma inteligente web e backend focada na otimização e automação da microgeração fotovoltaica integrada ao ecossistema de Mobilidade Elétrica (VE) da **GoodWe**.

A solução aborda o principal desafio da transição para veículos elétricos: **como otimizar o carregamento de VEs aproveitando 100% do excedente de energia solar gerada localmente**, reduzindo custos operacionais, mitigando picos de consumo na rede elétrica e minimizando a pegada de carbono.

---

## 👥 2. Equipe Envolvida
* **Nome:** Felipe Alves — **RM:** 572470
* * **Nome:** Pedro Henrique Andreaza — **RM:** 571107
* **Nome:** Eduardo Reis — **RM:** 569727
* **Nome:** Caio Eguia — **RM:** 570798

---

## 🏗️ 3. Arquitetura da Solução e Integração de Sistemas

A arquitetura foi estruturada no padrão **MVT (Model-View-Template)** utilizando o framework web **Django (Python)** e banco de dados relacional **SQLite**.

```
[ Inversor Fotovoltaico GoodWe (GW5000D-NS) ]
                 │
                 ▼
 [ Estação de Recarga GoodWe HCA (7.4kW) ]
                 │
                 ▼ (Leitura via API / Modbus TCP)
┌──────────────────────────────────────────────────────────┐
│                   BACKEND DJANGO                         │
│  - Engine de Cálculos de Custos (Tarifa kWh)             │
│  - Algoritmo de Priorização do Excedente Solar           │
│  - Assistente de IA Generativa & Análise Preditiva        │
└──────────────────────────┬───────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────┐
│              INTERFACE FRONTEND (GOODWI AI)              │
│  - /             -> Início (Menu de Navegação)            │
│  - /grafico/     -> Central de Recarga & Simulação VE    │
│  - /ia/          -> Assistente Virtual IA                │
│  - /perfil/      -> Parâmetros da Unidade Consumidora     │
│  - /sus/         -> Guia de Sustentabilidade & Métrica   │
└──────────────────────────────────────────────────────────┘
```

---

## 🧩 4. Módulos do Sistema e Funcionalidades

### 4.1. Central de Recarga & Otimização VE (`/grafico/`)
* **Finalidade:** Permitir ao utilizador simular e alternar modos de carregamento do Veículo Elétrico em tempo real.
* **O que faz:** 
  * **Simulador de Bateria VE:** Ajuste via slider de $10\%$ a $100\%$ do nível do veículo para estimativa exata do tempo restante de carga.
  * **Modo Eco Solar (100% Renovável):** Direciona exclusivamente o excedente dos painéis para a bateria do veículo (custo zero de rede).
  * **Modo Carga Rápida (Híbrido):** Combina potência solar com a rede convencional para carregamento rápido a $7.4\text{ kW}$.
  * **Gestão Inteligente de Demanda IA:** Evita recargas em horários de pico tarifário.
  * **Cálculo de Impacto:** Exibe a economia financeira em R$ e a redução de $\text{CO}_2$ evitado no período.

### 4.2. 🤖 Copiloto IA — O Piloto GoodWi AI (`/ia/`) — *O Grande Diferencial*
- **Finalidade:** Servir como um consultor inteligente e especialista no ecossistema GoodWe, mobilidade elétrica e sustentabilidade.
- **O que faz:** 
  * Responde instantaneamente a dúvidas técnicas sobre carregamento de carros e veículos elétricos (compatibilidade de conectores, ciclos de carga, vida útil da bateria automotiva).
  * Fornece orientações personalizadas sobre pegada de carbono, práticas ecológicas e eficiência na geração solar.
  * Orienta o cliente sobre alertas de demanda e manutenção preventiva de inversores, agindo proativamente como um verdadeiro piloto automatizado da instalação.
  
### 4.3. Unidade Consumidora & Equipamentos (`/perfil/`)
* **Finalidade:** Parametrizar as características técnicas da instalação e do contrato com a concessionária.
* **O que faz:** Armazena o modelo do inversor, a potência instalada ($\text{kWp}$), a tarifa de energia em $\text{R\$}/\text{kWh}$ (base do cálculo financeiro) e exibe o estado de conexão e firmware da estação GoodWe.

### 4.4. Dicas de Sustentabilidade & Recursos (`/sus/`)
* **Finalidade:** Educacional e institucional.
* **O que faz:** Apresenta boas práticas para maximizar a vida útil da bateria do veículo elétrico, preservar o inversor e fornece acessos diretos para entidades do setor (GoodWe, MME, ABSOLAR e ABVE).

---

## 🎯 5. Justificativa de Alinhamento ao Desafio GoodWe

| Requisito do Desafio | Solução Implementada no GoodWi AI |
| :--- | :--- |
| **Integração de Hardware GoodWe** | Mapeamento completo das especificações do Inversor GW5000D-NS e Estação VE HCA Series. |
| **Otimização Energética** | Algoritmo que prioriza o carregamento no pico solar ($10\text{h}$ às $15\text{h}$), eliminando o desperdício de injeção a baixo custo. |
| **Sustentabilidade Mensurável** | Conversão direta do consumo limpo em quilos de $\text{CO}_2$ evitados no meio ambiente. |
| **Usabilidade & Experiência** | Interface responsiva em Dark Mode com alto contraste visual e feedback em tempo real. |

---

## 📊 6. Resultados Quantitativos e Qualitativos

* **Economia Estimada:** Redução de até $70\%$ nos custos de carregamento veicular com o uso do Modo Eco Solar.
* **Redução de Carbono:** Estimativa média de eliminação de $156.0\text{ kg}$ de $\text{CO}_2$ por mês por veículo.
* **Ganho em Automação:** Eliminação da necessidade de intervenção manual do utilizador para pausar o carregamento em horários de pico.

---

## 🛠️ 7. Tecnologias, Frameworks e Ferramentas Utilizadas

* **Linguagem Backend:** Python 3.10+
* **Framework Web:** Django 4.x
* **Banco de Dados:** SQLite3
* **Frontend UI:** HTML5, CSS3, JavaScript (ES6+), Bootstrap 5, FontAwesome 6
* **Estilização Customizada:** Glassmorphism UI & Dark Theme de Alto Contraste

---

## 🚀 8. Como Executar o Projeto Localmente

1. **Clonar o Repositório:**
   ```bash
   git clone https://github.com/seu-usuario/goodwi-ai.git
   cd goodwi-ai
   ```

2. **Criar e Ativar um Ambiente Virtual (Venv):**
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. **Instalar as Dependências:**
   ```bash
   pip install django
   ```

4. **Executar as Migrações do Banco de Dados:**
   ```bash
   python manage.py migrate
   ```

5. **Iniciar o Servidor de Desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

6. **Acessar a Aplicação:**
   Abra o navegador e acesse `http://127.0.0.1:8000/`.
