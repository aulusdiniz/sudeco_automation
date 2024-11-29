
Feature: Certificado de Regularidade do FGTS – CRF

    @pending
    Scenario Outline: Certificado de Regularidade do FGTS – CRF
        Given O portal de consulta de Regularidade do Empregador é acessado
        When O campo <cnpj> para consulta CRF é preenchido
        And O UF do estado <uf> é informado
        And Aguardando o preenchimento do Recaptcha
        And A opção Consultar é selecionada
      # Aguardando dados consistentes

    Examples:
      | cnpj           | uf |
      | 30805662000108 | DF |

