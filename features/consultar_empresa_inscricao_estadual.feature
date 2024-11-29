
Feature: Consulta CNPJ da empresa pelo nº da Inscrição Estadual

    @ok #Aguardando dados consistentes
    Scenario Outline: Consulta CNPJ da empresa pelo nº da Inscrição Estadual
        Given O portal SINTEGRA é acessado
        When O estado <estado> é informado
        And O tipo de documento é selecionado
        And O campo <cnpj> para Consulta Pública ao Cadastro de Contribuintes é preenchido
        And O botão consultar CNPJ é selecionado
        Then Os dados são apresentados
        Then O arquivo Consulta CNPJ da empresa é salvo

    Examples:
      | cnpj           | estado |
      | 07191574000133 | Goiás  |

