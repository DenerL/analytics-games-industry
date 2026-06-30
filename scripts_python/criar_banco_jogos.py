import sqlite3

def criar_banco():
    # Conecta ou cria o arquivo do banco de dados
    conn = sqlite3.connect('portfolio_games.db')
    cursor = conn.cursor()
    
    # 1. Criação da tabela principal de Jogos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jogos (
            id INTEGER PRIMARY KEY,
            jogo TEXT NOT NULL,
            genero TEXT,
            jogabilidade_nota REAL,
            horas_semana REAL,
            idade_media INTEGER,
            gasto_mensal_brl REAL,
            fator_compra TEXT,
            satisfacao INTEGER,
            qtd_biblioteca_perfil INTEGER,
            taxa_conclusao REAL
        )
    ''')
    
    # 2. Criação da tabela de ligação para Multiplataformas (PC, Console, Switch 2, Mobile)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jogo_plataforma (
            jogo_id INTEGER,
            plataforma TEXT,
            PRIMARY KEY (jogo_id, plataforma),
            FOREIGN KEY (jogo_id) REFERENCES jogos (id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Banco de dados 'portfolio_games.db' criado com sucesso!")

if __name__ == "__main__":
    criar_banco()