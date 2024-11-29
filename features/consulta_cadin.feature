
Feature: Cadastro Informativo de Créditos não Quitados do Setor Público Federal - CADIN

    @pending
    Scenario Outline: Cadastro Informativo de Créditos não Quitados do Setor Público Federal - CADIN
        Given O portal de consulta do CADIN é acessado
        When O login via gov.br é selecionado
        And O campo <cpf_cnpj> para o login gov.br é preenchido
        And O botão continuar é selecionado
        And Aguardando o preenchimento do Recaptcha
#        Aguardando solução Recaptcha #Erro

    Examples:
      | cpf_cnpj       |
      | 30805662000108 |

