import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import psycopg2
import mysql.connector
import csv
import os

class DatabaseExporterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Exportador de Consultas SQL para CSV - By Ailton Occhi")
        self.root.geometry("800x750")
        self.root.resizable(True, True)
        
        # caminho do arquivo
        self.caminho_arquivo = tk.StringVar()
        # tipo de banco de dados
        self.tipo_banco = tk.StringVar(value="postgresql")
        
        self.criar_interface()
    
    def criar_interface(self):
        # frame principal com margem
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # configuração da expansão da grade
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        row = 0
        
        # título
        titulo = ttk.Label(main_frame, text="Exportador de Dados para CSV", font=('Arial', 14, 'bold'))
        titulo.grid(row=row, column=0, columnspan=3, pady=(0, 20))
        row += 1
        
        # seção: tipo de banco de dados
        secao_tipo = ttk.LabelFrame(main_frame, text="Tipo de Banco de Dados", padding="10")
        secao_tipo.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        row += 1
        
        # botões para escolher o tipo de banco
        frame_radios = ttk.Frame(secao_tipo)
        frame_radios.grid(row=0, column=0, sticky=tk.W)
        
        radio_postgres = ttk.Radiobutton(frame_radios, text="PostgreSQL", 
                                        variable=self.tipo_banco, value="postgresql",
                                        command=self.atualizar_porta_padrao)
        radio_postgres.grid(row=0, column=0, padx=(0, 20))
        
        radio_mysql = ttk.Radiobutton(frame_radios, text="MySQL", 
                                     variable=self.tipo_banco, value="mysql",
                                     command=self.atualizar_porta_padrao)
        radio_mysql.grid(row=0, column=1)
        
        # seção: dados de conexão
        secao_conexao = ttk.LabelFrame(main_frame, text="Dados de Conexão", padding="10")
        secao_conexao.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        secao_conexao.columnconfigure(1, weight=1)
        row += 1
        
        # host
        ttk.Label(secao_conexao, text="Host:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entry_host = ttk.Entry(secao_conexao, width=40)
        self.entry_host.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(5, 0), pady=5)
        self.entry_host.insert(0, "localhost")
        
        # porta
        ttk.Label(secao_conexao, text="Porta:").grid(row=0, column=2, sticky=tk.W, padx=(10, 0), pady=5)
        self.entry_porta = ttk.Entry(secao_conexao, width=10)
        self.entry_porta.grid(row=0, column=3, sticky=tk.W, padx=(5, 0), pady=5)
        self.entry_porta.insert(0, "5432")
        
        # banco de dados
        ttk.Label(secao_conexao, text="Banco:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_database = ttk.Entry(secao_conexao, width=40)
        self.entry_database.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(5, 0), pady=5)
        self.entry_database.insert(0, "postgres")
        
        # usuário
        ttk.Label(secao_conexao, text="Usuário:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.entry_usuario = ttk.Entry(secao_conexao, width=40)
        self.entry_usuario.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(5, 0), pady=5)
        self.entry_usuario.insert(0, "root")
        
        # senha
        ttk.Label(secao_conexao, text="Senha:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.entry_senha = ttk.Entry(secao_conexao, width=40, show="*")
        self.entry_senha.grid(row=3, column=1, sticky=(tk.W, tk.E), padx=(5, 0), pady=5)
        
        # botão testar conexão
        btn_testar = ttk.Button(secao_conexao, text="Testar Conexão", command=self.testar_conexao)
        btn_testar.grid(row=3, column=2, columnspan=2, padx=(10, 0), pady=5)
        
        # seção: consulta sql
        secao_sql = ttk.LabelFrame(main_frame, text="Consulta SQL", padding="10")
        secao_sql.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        secao_sql.columnconfigure(0, weight=1)
        secao_sql.rowconfigure(1, weight=1)
        main_frame.rowconfigure(row, weight=1)
        row += 1
        
        ttk.Label(secao_sql, text="Cole sua consulta SQL abaixo:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        self.text_sql = scrolledtext.ScrolledText(secao_sql, width=80, height=12, wrap=tk.WORD)
        self.text_sql.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # seção: configuração do arquivo csv
        secao_arquivo = ttk.LabelFrame(main_frame, text="Configuração do Arquivo CSV", padding="10")
        secao_arquivo.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        secao_arquivo.columnconfigure(1, weight=1)
        row += 1
        
        # nome do arquivo
        ttk.Label(secao_arquivo, text="Nome do arquivo:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entry_nome_arquivo = ttk.Entry(secao_arquivo)
        self.entry_nome_arquivo.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(5, 0), pady=5)
        self.entry_nome_arquivo.insert(0, "resultados.csv")
        
        # local para salvar
        ttk.Label(secao_arquivo, text="Local:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_caminho = ttk.Entry(secao_arquivo, textvariable=self.caminho_arquivo)
        self.entry_caminho.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(5, 5), pady=5)
        
        btn_procurar = ttk.Button(secao_arquivo, text="Procurar...", command=self.selecionar_local)
        btn_procurar.grid(row=1, column=2, pady=5)
        
        # botão exportar
        btn_exportar = ttk.Button(main_frame, text="Exportar para CSV", command=self.exportar_dados)
        btn_exportar.grid(row=row, column=0, columnspan=3, pady=(10, 0), ipadx=20, ipady=5)
        
        # barra de status no rodapé
        self.status_var = tk.StringVar()
        self.status_var.set("Pronto")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, 
                              relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=row+1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
    
    def atualizar_porta_padrao(self):
        """Atualiza a porta padrão conforme o tipo de banco selecionado"""
        if self.tipo_banco.get() == "postgresql":
            self.entry_porta.delete(0, tk.END)
            self.entry_porta.insert(0, "5432")
        else:  # mysql
            self.entry_porta.delete(0, tk.END)
            self.entry_porta.insert(0, "3306")
    
    def conectar_banco(self):
        """Conecta ao banco de dados conforme o tipo selecionado"""
        if self.tipo_banco.get() == "postgresql":
            return psycopg2.connect(
                host=self.entry_host.get(),
                port=int(self.entry_porta.get()),
                database=self.entry_database.get(),
                user=self.entry_usuario.get(),
                password=self.entry_senha.get()
            )
        else:  # mysql
            return mysql.connector.connect(
                host=self.entry_host.get(),
                port=int(self.entry_porta.get()),
                database=self.entry_database.get(),
                user=self.entry_usuario.get(),
                password=self.entry_senha.get()
            )
    
    def testar_conexao(self):
        """Testa a conexão com o banco de dados"""
        try:
            self.status_var.set("Testando conexão...")
            self.root.update()
            
            conn = self.conectar_banco()
            conn.close()
            
            tipo_nome = "PostgreSQL" if self.tipo_banco.get() == "postgresql" else "MySQL"
            self.status_var.set(f"Conexão {tipo_nome} bem-sucedida!")
            messagebox.showinfo("Sucesso", f"Conexão com o banco de dados {tipo_nome} estabelecida com sucesso!")
        except Exception as e:
            self.status_var.set("Erro na conexão")
            messagebox.showerror("Erro de Conexão", f"Não foi possível conectar ao banco de dados:\n\n{str(e)}")
    
    def selecionar_local(self):
        """Abre diálogo para selecionar o local para salvar o arquivo"""
        local = filedialog.askdirectory(title="Selecione o local para salvar o arquivo CSV")
        if local:
            self.caminho_arquivo.set(local)
    
    def executar_consulta_e_exportar(self):
        """Executa a consulta SQL e exporta para CSV"""
        # validação dos campos obrigatórios
        if not self.entry_host.get():
            messagebox.showwarning("Atenção", "Informe o host do banco de dados.")
            return
        
        if not self.entry_database.get():
            messagebox.showwarning("Atenção", "Informe o nome do banco de dados.")
            return
        
        if not self.entry_usuario.get():
            messagebox.showwarning("Atenção", "Informe o usuário.")
            return
        
        sql = self.text_sql.get("1.0", tk.END).strip()
        if not sql:
            messagebox.showwarning("Atenção", "Informe a consulta SQL.")
            return
        
        if not self.entry_nome_arquivo.get():
            messagebox.showwarning("Atenção", "Informe o nome do arquivo.")
            return
        
        if not self.caminho_arquivo.get():
            messagebox.showwarning("Atenção", "Selecione um local para salvar o arquivo CSV.")
            return
        
        # define o caminho completo do arquivo
        nome_arquivo = self.entry_nome_arquivo.get()
        if not nome_arquivo.endswith('.csv'):
            nome_arquivo += '.csv'
        
        caminho_completo = os.path.join(self.caminho_arquivo.get(), nome_arquivo)
        
        try:
            # conectar no banco
            tipo_nome = "PostgreSQL" if self.tipo_banco.get() == "postgresql" else "MySQL"
            self.status_var.set(f"Conectando ao banco de dados {tipo_nome}...")
            self.root.update()
            
            conn = self.conectar_banco()
            
            # executa a consulta sql
            self.status_var.set("Executando consulta SQL...")
            self.root.update()
            
            cursor = conn.cursor()
            cursor.execute(sql)
            
            # pega os resultados
            colunas = [desc[0] for desc in cursor.description]
            resultados = cursor.fetchall()
            
            cursor.close()
            conn.close()
            
            if not resultados:
                self.status_var.set("Consulta não retornou resultados")
                messagebox.showinfo("Aviso", "A consulta não retornou nenhum resultado.")
                return
            
            # exporta os dados para csv
            self.status_var.set(f"Exportando {len(resultados)} registros para CSV...")
            self.root.update()
            
            with open(caminho_completo, 'w', newline='', encoding='utf-8') as arquivo_csv:
                escritor = csv.writer(arquivo_csv, delimiter=';')
                escritor.writerow(colunas)
                escritor.writerows(resultados)
            
            self.status_var.set(f"Exportação concluída! {len(resultados)} registros exportados.")
            messagebox.showinfo("Sucesso", 
                              f"Dados exportados com sucesso!\n\n"
                              f"Arquivo: {caminho_completo}\n"
                              f"Registros: {len(resultados)}\n"
                              f"Colunas: {len(colunas)}")
            
        except Exception as e:
            self.status_var.set("Erro durante a exportação")
            messagebox.showerror("Erro", f"Erro durante a exportação:\n\n{str(e)}")
    
    def exportar_dados(self):
        """Inicia o processo de exportação"""
        self.executar_consulta_e_exportar()

def main():
    root = tk.Tk()
    app = DatabaseExporterGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()