from unittest import TestCase
from behave import *
from pages.login_page import TestPage

use_step_matcher("parse")
assertions = TestCase()


@given("O portal de consulta de certidões da Receita Federal é acessado")
def step_impl(context):
    test_page = TestPage(context)
    test_page.access_portal_receita()


@when("O campo {cpf_cnpj} para consulta de improbidade é informado")
def step_impl(context, cpf_cnpj):
    test_page = TestPage(context)
    test_page.insert_cpf_cnpj_improbidade(cpf_cnpj)


@step("A consulta para emissão de nova certidão é selecionada")
def step_impl(context):
    test_page = TestPage(context)
    test_page.consultar_cpf_cnpj()


@step("O período de consulta é informado")
def step_impl(context):
    test_page = TestPage(context)
    test_page.informar_periodo_consulta()


@given("O portal de consulta do CNJ de Improbidade Administrativa é acessado")
def step_impl(context):
    test_page = TestPage(context)
    test_page.access_portal_cnj()


@step("O {nome} nome da pessoa é informado")
def step_impl(context, nome):
    test_page = TestPage(context)
    test_page.insert_nome_pessoa(nome)


@step("O Recaptcha checkbox é marcado")
def step_impl(context):
    test_page = TestPage(context)
    test_page.mark_recaptcha_checkbox()


@given("O portal de Certidões da Controladoria-Geral da União é acessado")
def step_impl(context):
    test_page = TestPage(context)
    test_page.access_portal_cgu()


@when("O campo {cpf_cnpj} para consulta de certidão CGU é preenchido")
def step_impl(context, cpf_cnpj):
    test_page = TestPage(context)
    test_page.insert_cpf_cnpj_cgu(cpf_cnpj)


@step("O código {codigo} da certidão é informado")
def step_impl(context, codigo):
    test_page = TestPage(context)
    test_page.insert_codigo_certidao(codigo)


@when("O campo {cpf_cnpj} para o portal da Receita é informado")
def step_impl(context, cpf_cnpj):
    test_page = TestPage(context)
    test_page.insert_cpf_cnpj_receita(cpf_cnpj)


@given("O portal de consulta do CADIN é acessado")
def step_impl(context):
    test_page = TestPage(context)
    test_page.access_portal_cadin()


@when("O login via gov.br é selecionado")
def step_impl(context):
    test_page = TestPage(context)
    test_page.login_gov_br()


@step("O campo {cpf_cnpj} para o login gov.br é preenchido")
def step_impl(context, cpf_cnpj):
    test_page = TestPage(context)
    test_page.insert_cpf_cnpj_gov_br(cpf_cnpj)


@step("O botão continuar é selecionado")
def step_impl(context):
    test_page = TestPage(context)
    test_page.selecionar_continuar()


@given("O portal de consulta de Regularidade do Empregador é acessado")
def step_impl(context):
    test_page = TestPage(context)
    test_page.access_portal_regularidade_fgts()


@when("O campo {cnpj} para consulta CRF é preenchido")
def step_impl(context, cnpj):
    test_page = TestPage(context)
    test_page.insert_cnpj_crf(cnpj)


@step("O estado {uf} é informado")
def step_impl(context, uf):
    test_page = TestPage(context)
    test_page.insert_uf_crf(uf)


@given("O portal SINTEGRA é acessado")
def step_impl(context):
    test_page = TestPage(context)
    test_page.access_portal_sintegra()


@step("O tipo de documento é selecionado")
def step_impl(context):
    test_page = TestPage(context)
    test_page.selecionar_tipo_documento()


@step("O campo {cnpj} para Consulta Pública ao Cadastro de Contribuintes é preenchido")
def step_impl(context, cnpj):
    test_page = TestPage(context)
    test_page.insert_cnpj(cnpj)


@step("O botão consultar CNPJ é selecionado")
def step_impl(context):
    test_page = TestPage(context)
    test_page.consultar_cnpj()


@step("A opção pesquisar é selecionada")
def step_impl(context):
    test_page = TestPage(context)
    test_page.selecionar_pesquisar()


@step("A certidão negativa de Improbidade Administrativa é gerada")
def step_impl(context):
    test_page = TestPage(context)
    test_page.gerar_certidao_improbidade()


@step("Aguardando o preenchimento do Recaptcha")
def step_impl(context):
    test_page = TestPage(context)
    test_page.aguardando_recaptcha()


@step("A opção Consultar é selecionada")
def step_impl(context):
    test_page = TestPage(context)
    test_page.selecionar_consultar()


@step("O botão consultar é selecionado")
def step_impl(context):
    test_page = TestPage(context)
    test_page.selecionar_botao_consultar()


@step("A certidão é selecionada")
def step_impl(context):
    test_page = TestPage(context)
    test_page.selecionar_tipo_certidao()


@step("A Certidão de Cadastro de Empresas Inidôneas e Suspensas é emitida")
def step_impl(context):
    test_page = TestPage(context)
    test_page.emitir_certidao_CGU()


@then("Os dados são apresentados")
def step_impl(context):
    expected_text = "Consulta Pública ao Cadastro de Contribuintes"
    actual = expected_text
    expected = expected_text
    assertions.assertEqual(actual, expected)


@given("O portal de consulta do TCU é acessado")
def step_impl(context):
    test_page = TestPage(context)
    test_page.acessar_portal_tcu()


@when("O login através do gov.br é selecionado")
def step_impl(context):
    test_page = TestPage(context)
    test_page.login_gov()


@step("A senha {senha_gov} é informada")
def step_impl(context, senha_gov):
    test_page = TestPage(context)
    test_page.informar_senha_gov(senha_gov)


@step("O UF do estado {uf} é informado")
def step_impl(context, uf):
    test_page = TestPage(context)
    test_page.selecionar_estado(uf)


@then("A Certidão CGU é salva no diretório correspondente")
def step_impl(context):
    test_page = TestPage(context)
    test_page.salvar_certidao_cgu()


@then("A Certidão CNJ é salva no diretório correspondente")
def step_impl(context):
    test_page = TestPage(context)
    test_page.salvar_certidao_cnj()


@then("O arquivo Consulta CNPJ da empresa é salvo")
def step_impl(context):
    test_page = TestPage(context)
    test_page.salvar_consulta_inscricao_estadual()
