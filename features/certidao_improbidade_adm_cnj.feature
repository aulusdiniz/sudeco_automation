
Feature: Certidão de Improbidade Administrativa - CNJ

    @ok
    Scenario Outline: Certidão de Improbidade Administrativa - CNJ
        Given O portal de consulta do CNJ de Improbidade Administrativa é acessado
        When O campo <cpf_cnpj> para consulta de improbidade é informado
        And O <nome> nome da pessoa é informado
        And O Recaptcha checkbox é marcado
        And Aguardando o preenchimento do Recaptcha
        And A opção pesquisar é selecionada
        And A certidão negativa de Improbidade Administrativa é gerada
        Then A Certidão CNJ é salva no diretório correspondente


    Examples:
      | cpf_cnpj       | nome                                              |
      | 30805662000108 | PMT - Photonex Comércio de Material Elétrico LTDA |


