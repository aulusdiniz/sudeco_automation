
Feature: Certidão de Cadastro Empresas Inidôneas – TCU

    @pending
    Scenario Outline: Certidão de Cadastro Empresas Inidôneas – TCU
        Given O portal de consulta do TCU é acessado
        When O login através do gov.br é selecionado
        And O campo <cpf_cnpj> para o login gov.br é preenchido
        And O botão continuar é selecionado
        And Aguardando o preenchimento do Recaptcha
#        Aguardando solução Recaptcha #Erro



    Examples:
      | cpf_cnpj       |
      | 30805662000108 |

