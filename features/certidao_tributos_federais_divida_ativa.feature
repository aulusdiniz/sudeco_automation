
Feature: Certidão de Tributos Federais e Dívida Ativa da União

    @pending # Dados Inconsistentes
    Scenario Outline: Emissão de Certidão de Tributos Federais e Dívida Ativa da União - CPF/CNPJ
        Given O portal de consulta de certidões da Receita Federal é acessado
        When O campo <cpf_cnpj> para o portal da Receita é informado
        And O período de consulta é informado
        And A consulta para emissão de nova certidão é selecionada
#        Consulta Indisponível - Erro ou dados inconsistentes.
#        And O arquivo PDF é gerado e anexado na pasta de acompanhamento da empresa
#        Then O arquivo da certidão emitida é salvo

    Examples:
      | cpf_cnpj       |
      | 30682758000118 |

