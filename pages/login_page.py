import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lib.selenium_helper import Helpers
import tkinter as tk
from pynput import mouse
import threading
import time
import shutil


class TestPage:
    def __init__(self, context):
        self.context = context
        self.helper = Helpers(context)

    os.environ.setdefault("TERM", "xterm")

    def select_search_button(self):
        self.helper.selenium_wait_clickable(2, By.ID, 'APjFqb')
        self.context.browser.find_element(By.ID, 'APjFqb').click()

    def insert_iphone_model(self, iphone_model):
        search_box = self.context.browser.find_element(By.ID, 'APjFqb')
        search_box.send_keys(iphone_model)
        actions = ActionChains(self.context.browser)
        actions.move_to_element(search_box).send_keys(Keys.ENTER).perform()

    def select_shopping_sheet(self):
        self.helper.selenium_wait_clickable(2, By.PARTIAL_LINK_TEXT, 'Shopping')
        shopping_button = self.context.browser.find_element(By.PARTIAL_LINK_TEXT, 'Shopping')
        shopping_button.click()

    def access_portal_receita(self):
        self.context.browser.get('https://solucoes.receita.fazenda.gov.br/Servicos/certidaointernet/PJ/Consultar')

    def consultar_cpf_cnpj(self):
        consultar_button = self.context.browser.find_element(By.ID, 'validar')
        consultar_button.click()

    def informar_periodo_consulta(self):
        self.helper.selenium_wait_clickable(2, By.CSS_SELECTOR, "#PeriodoInicio")
        periodo_inicial_box = self.context.browser.find_element(By.CSS_SELECTOR, '#PeriodoInicio')
        periodo_inicial_box.send_keys("01/10/2018")
        periodo_final_box = self.context.browser.find_element(By.CSS_SELECTOR, '#PeriodoFim')
        periodo_final_box.send_keys("01/12/2018")

    def access_portal_cnj(self):
        self.context.browser.get('https://www.cnj.jus.br/improbidade_adm/consultar_requerido.php')

    def insert_cpf_cnpj_improbidade(self, cpf_cnpj):
        self.helper.selenium_wait_clickable(2, By.CSS_SELECTOR, "#num_cpf_cnpj")
        input_box = self.context.browser.find_element(By.CSS_SELECTOR, '#num_cpf_cnpj')
        input_box.send_keys(cpf_cnpj)

    def insert_nome_pessoa(self, nome):
        self.helper.selenium_wait_clickable(2, By.CSS_SELECTOR, "#nom_requerido")
        input_box = self.context.browser.find_element(By.CSS_SELECTOR, '#nom_requerido')
        input_box.send_keys(nome)

    def mark_recaptcha_checkbox(self):
        self.helper.selenium_wait_presence(2, By.XPATH,
                                           "/html/body/div[2]/div[5]/form/table/tbody/tr[5]/td/div[2]/div/div/iframe")
        modal_frame = self.context.browser.find_element(By.XPATH,
                                                        "/html/body/div[2]/div[5]/form/table/tbody/tr[5]/td/div[2]/div/div/iframe")
        self.context.browser.switch_to.frame(modal_frame)
        recaptcha_checkbox = self.context.browser.find_element(By.CSS_SELECTOR,
                                                               '#recaptcha-anchor > div.recaptcha-checkbox-border')
        recaptcha_checkbox.click()

    def access_portal_cgu(self):
        self.context.browser.get('https://certidoes.cgu.gov.br/')

    def insert_cpf_cnpj_cgu(self, cpf_cnpj):
        self.helper.selenium_wait_clickable(2, By.CSS_SELECTOR, "#cpfCnpj")
        input_box = self.context.browser.find_element(By.CSS_SELECTOR, '#cpfCnpj')
        input_box.send_keys(cpf_cnpj)

    def insert_codigo_certidao(self, codigo):
        self.helper.selenium_wait_clickable(2, By.CSS_SELECTOR, "#codigoCertidao")
        input_box = self.context.browser.find_element(By.CSS_SELECTOR, '#codigoCertidao')
        input_box.send_keys(codigo)

    def insert_cpf_cnpj_receita(self, cpf_cnpj):
        self.helper.selenium_wait_clickable(2, By.CSS_SELECTOR, "#Ni")
        input_box = self.context.browser.find_element(By.CSS_SELECTOR, '#Ni')
        input_box.send_keys(cpf_cnpj)

    def access_portal_cadin(self):
        self.context.browser.get('https://cadin.pgfn.gov.br/')

    def login_gov_br(self):
        self.helper.selenium_wait_clickable(2, By.XPATH,
                                            "/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/ion-grid/ion-row/ion-col[2]/ion-row[2]/ion-col/div[2]/button")
        login_gov_br_button = self.context.browser.find_element(By.XPATH,
                                                                '/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/ion-grid/ion-row/ion-col[2]/ion-row[2]/ion-col/div[2]/button')
        login_gov_br_button.click()

    def insert_cpf_cnpj_gov_br(self, cpf_cnpj):
        self.helper.selenium_wait_clickable(2, By.CSS_SELECTOR, "#accountId")
        input_box = self.context.browser.find_element(By.CSS_SELECTOR, '#accountId')
        input_box.send_keys(cpf_cnpj)

    def selecionar_continuar(self):
        login_gov_br_button = self.context.browser.find_element(By.CSS_SELECTOR, '#enter-account-id')
        login_gov_br_button.click()

    def access_portal_regularidade_fgts(self):
        self.context.browser.get('https://consulta-crf.caixa.gov.br/consultacrf/pages/consultaEmpregador.jsf')

    def insert_cnpj_crf(self, cnpj):
        self.helper.selenium_wait_clickable(2, By.CSS_SELECTOR, "#mainForm\:txtInscricao1")
        input_box = self.context.browser.find_element(By.CSS_SELECTOR, '#mainForm\:txtInscricao1')
        input_box.send_keys(cnpj)

    def insert_uf_crf(self, uf):
        if uf == "Acre":
            self.context.browser.get('https://sefazonline.ac.gov.br/sefazonline/app.wmsintegralista')
        elif uf == "Alagoas":
            self.context.browser.get('https://sintegra.sefaz.al.gov.br/')
        elif uf == "Amapá":
            self.context.browser.get('http://www.sefaz.ap.gov.br/sate/seg/SEGf_AcessarFuncao.jsp?cdFuncao=CAD_011')
        elif uf == "Amazonas":
            self.context.browser.get('https://www.sefaz.am.gov.br/sintegra/sintegra0.asp')
        elif uf == "Bahia":
            self.context.browser.get('http://www.sefaz.ba.gov.br/Sintegra/sintegra.asp?estado=BA')
        elif uf == "Ceará":
            self.context.browser.get('https://consultapublica.sefaz.ce.gov.br/sintegra/preparar-consultar')
        elif uf == "Distrito Federal":
            self.context.browser.get('https://ww1.receita.fazenda.df.gov.br/icms/sintegra-consulta')
        elif uf == "Espírito Santo":
            self.context.browser.get('http://www.sintegra.es.gov.br/Siplag4/faces/login.jsp')
        elif uf == "Goiás":
            self.context.browser.get('http://appasp.sefaz.go.gov.br/Sintegra/Consulta/default.html')
        elif uf == "Maranhão":
            self.context.browser.get(
                'http://aplicacoes.ma.gov.br/sintegra/jsp/consultaSintegra/consultaSintegraFiltro.jsf')
        elif uf == "Mato Grosso":
            self.context.browser.get(
                'https://www.sefaz.mt.gov.br/cadastro/emissaocartao/emissaocartaocontribuinteacessodireto')
        elif uf == "Mato Grosso do Sul":
            self.context.browser.get('http://www1.sefaz.ms.gov.br/Cadastro/sintegra/cadastromsCCI.asp')
        elif uf == "Minas Gerais":
            self.context.browser.get('https://dfe-portal.svrs.rs.gov.br/NFE/CCC')
        elif uf == "Pará":
            self.context.browser.get('https://app.sefa.pa.gov.br/sintegra/')
        elif uf == "Paraíba":
            self.context.browser.get('https://www4.sefaz.pb.gov.br/sintegra/SINf_ConsultaSintegra.jsp')
        elif uf == "Paraná":
            self.context.browser.get('http://www.sintegra.fazenda.pr.gov.br/sintegra/')
        elif uf == "Pernambuco":
            self.context.browser.get('http://www.sintegra.sefaz.pe.gov.br/servdados/login.php')
        elif uf == "Piauí":
            self.context.browser.get('http://web.sintegra.sefaz.pi.gov.br/')
        elif uf == "Rio de Janeiro":
            self.context.browser.get('https://sincad-web.fazenda.rj.gov.br/sincad-web/index.jsf')
        elif uf == "Rio Grande do Norte":
            self.context.browser.get('https://www.sefaz.rn.gov.br/uvt/consultacontribuinte.aspx')
        elif uf == "Rio Grande do Sul":
            self.context.browser.get('https://www.sefaz.rs.gov.br/consultas/contribuinte')
        elif uf == "Rondônia":
            self.context.browser.get('https://portalcontribuinte.sefin.ro.gov.br/Publico/parametropublica.jsp')
        elif uf == "Roraima":
            self.context.browser.get('https://portalapp.sefaz.rr.gov.br/siate/servlet/wp_siate_consultasintegra')
        elif uf == "Santa Catarina":
            self.context.browser.get('https://sat.sef.sc.gov.br/tax.NET/Sat.Cadastro.Web/ComprovanteIE/Consulta.aspx')
        elif uf == "São Paulo":
            self.context.browser.get(
                'https://www.cadesp.fazenda.sp.gov.br/(S(2phwakz5ktke5jrfucwkzvhj))/Pages/Cadastro/Consultas/ConsultaPublica/ConsultaPublica.aspx')
        elif uf == "Sergipe":
            self.context.browser.get('https://security.sefaz.se.gov.br/SIC/sintegra/index.jsp')
        elif uf == "Tocantins":
            self.context.browser.get('https://sintegra.sefaz.to.gov.br/sintegra/servlet/wpsico01')
        elif uf == "Suframa":
            self.context.browser.get('https://wwws.suframa.gov.br/sintegra/')

    def access_portal_sintegra(self):
        self.context.browser.get('https://www.sintegra.gov.br/')

    def selecionar_tipo_documento(self):
        self.helper.selenium_wait_clickable(2, By.CSS_SELECTOR, "#rTipoDocCNPJ")
        cnpj_ratio = self.context.browser.find_element(By.CSS_SELECTOR, "#rTipoDocCNPJ")
        cnpj_ratio.click()

    def insert_cnpj(self, cnpj):
        cnpj_box = self.context.browser.find_element(By.CSS_SELECTOR, '#tCNPJ')
        cnpj_box.send_keys(cnpj)

    def consultar_cnpj(self):
        consultar_button = self.context.browser.find_element(By.XPATH, '/html/body/form/div/div[2]/input[1]')
        consultar_button.click()

    def selecionar_pesquisar(self):
        time.sleep(30)
        self.context.browser.switch_to.default_content()
        botao_pesquisar = self.context.browser.find_element(By.ID, "btnPesquisarRequerido")
        botao_pesquisar.click()

    def gerar_certidao_improbidade(self):
        self.helper.selenium_wait_clickable(2, By.ID, "btnCertidaoNegativa")
        botao_gerar_certidao = self.context.browser.find_element(By.ID, "btnCertidaoNegativa")
        botao_gerar_certidao.click()

    def aguardando_recaptcha(self):
        def monitor_mouse():
            last_time = time.time()

            def on_move(x, y):
                nonlocal last_time
                current_time = time.time()

                if current_time - last_time >= 0.5:
                    root.destroy()
                else:
                    last_time = current_time

            with mouse.Listener(on_move=on_move) as listener:
                listener.join()

        root = tk.Tk()

        root.overrideredirect(True)

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        window_width = 800  # 400 * 2
        window_height = 600  # 300 * 2

        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)

        root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        root.configure(bg="red")

        def blink_window():
            current_color = root.cget("bg")
            new_color = "red" if current_color == "black" else "black"
            root.configure(bg=new_color)
            root.after(500, blink_window)

        message_label = tk.Label(
            root,
            text="Resolva o reCAPTCHA",
            font=("Arial", 24, "bold"),
            bg="red",
            fg="white"
        )

        message_label.place(relx=0.5, rely=0.5, anchor="center")

        mouse_thread = threading.Thread(target=monitor_mouse, daemon=True)
        mouse_thread.start()

        blink_window()

        root.mainloop()

    def selecionar_consultar(self):
        time.sleep(30)
        self.context.browser.find_element(By.ID, "mainForm:btnConsultar").click()

    def selecionar_botao_consultar(self):
        self.context.browser.find_element(By.ID, "consultar").click()

    def selecionar_tipo_certidao(self):
        ratio_certidao = self.context.browser.find_element(By.XPATH,
                                                           "/html/body/div[1]/section/section/div/div/div[2]/div/div[4]/div/div/table/tbody/tr/td[1]/div/input")
        ratio_certidao.click()

    def emitir_certidao_CGU(self):
        time.sleep(12)
        botao_emitir_certidao = self.context.browser.find_element(By.XPATH,
                                                                  "/html/body/div[1]/section/div/section/div/table/tbody/tr[1]/td[4]/button")
        botao_emitir_certidao.click()

    def acessar_portal_tcu(self):
        self.context.browser.get('https://siga.apps.tcu.gov.br/')

    def salvar_certidao_cgu(self):
        download_dir = os.path.join(os.getcwd(), "default_download_location")
        files = [os.path.join(download_dir, f) for f in os.listdir(download_dir) if
                 os.path.isfile(os.path.join(download_dir, f))]

        if not files:
            raise FileNotFoundError("Nenhum arquivo encontrado no diretório de downloads.")

        latest_file = max(files, key=os.path.getmtime)
        destination_path = os.path.join(self.context.download_directory, os.path.basename(latest_file))
        shutil.move(latest_file, destination_path)
        print(f"Arquivo salvo em: {destination_path}")

    def salvar_certidao_cnj(self):
        download_dir = os.path.join(os.getcwd(), "default_download_location")
        files = [os.path.join(download_dir, f) for f in os.listdir(download_dir) if
                 os.path.isfile(os.path.join(download_dir, f))]

        if not files:
            raise FileNotFoundError("Nenhum arquivo encontrado no diretório de downloads.")

        latest_file = max(files, key=os.path.getmtime)
        destination_path = os.path.join(self.context.download_directory, os.path.basename(latest_file))
        shutil.move(latest_file, destination_path)
        print(f"Arquivo salvo em: {destination_path}")

    def salvar_consulta_inscricao_estadual(self):
        actions = ActionChains(self.context.browser)
        actions.key_down(Keys.CONTROL).send_keys('p').key_up(Keys.CONTROL).perform()
        actions.send_keys(Keys.ENTER).perform()

    def login_gov(self):
        self.helper.selenium_wait_clickable(2, By.ID, "govbr")
        botao_login_gov = self.context.browser.find_element(By.ID, "govbr")
        botao_login_gov.click()

    def informar_senha_gov(self, senha_gov):
        self.helper.selenium_wait_clickable(2, By.ID, "govbr")
        senha_gov = self.context.browser.find_element(By.ID, "govbr")
        senha_gov.send_keys(senha_gov)

    def selecionar_estado(self, uf):
        self.helper.selenium_wait_clickable(2, By.ID, "mainForm:uf")
        dropdown_uf = self.context.browser.find_element(By.ID, "mainForm:uf")
        dropdown_uf.send_keys(uf)
