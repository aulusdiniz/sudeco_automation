
Feature: Certidão de Cadastro de Empresas Inidôneas e Suspensas - CGU

    @ok
    Scenario Outline: Certidão de Cadastro de Empresas Inidôneas e Suspensas - CGU
        Given O portal de Certidões da Controladoria-Geral da União é acessado
        When O campo <cpf_cnpj> para consulta de certidão CGU é preenchido
        And A certidão é selecionada
        And O botão consultar é selecionado
        And A Certidão de Cadastro de Empresas Inidôneas e Suspensas é emitida
        Then A Certidão CGU é salva no diretório correspondente

    Examples:
      | cpf_cnpj       |
      | 30805662000108 |

