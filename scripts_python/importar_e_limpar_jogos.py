import sqlite3
import pandas as pd

def importar_e_ranquear_jogos():
    nome_arquivo = 'projeto1.jogos.xlsx'
    try:
        df = pd.read_excel(nome_arquivo)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return

    # --- ENGENHARIA DE DADOS: CÁLCULO DO RANKING AUTOMÁTICO ---
    # Criamos um score baseado em engajamento, nota e conclusão
    # Preenchemos valores zerados com a média para não quebrar o cálculo
    horas = df['Horas_Semana'].fillna(df['Horas_Semana'].mean())
    nota = df['Jogabilidade_Nota'].fillna(df['Jogabilidade_Nota'].mean())
    conclusao = df['Taxa_Conclusao'].fillna(df['Taxa_Conclusao'].mean())
    
    # Fórmula do Score: Horas semanais têm peso maior, multiplicado pela nota e taxa de término
    df['score_engajamento'] = (horas * 0.5) + (nota * 0.3) + (conclusao * 0.2)
    
    # Ordena do maior score para o menor e cria o Ranking de 1 a 100
    df = df.sort_values(by='score_engajamento', ascending=False).reset_index(drop=True)
    df['posicao_ranking'] = df.index + 1
    # ----------------------------------------------------------

    conn = sqlite3.connect('portfolio_games.db')
    cursor = conn.cursor()

    # Adiciona a coluna de ranking na tabela jogos caso ela não exista
    try:
        cursor.execute('ALTER TABLE jogos ADD COLUMN posicao_ranking INTEGER')
    except sqlite3.OperationalError:
        # Se a coluna já existir, o SQLite avisa e o código ignora o erro para continuar
        pass

    print("Calculando ranking e importando dados tratados...")

    for index, linha in df.iterrows():
        jogo_nome = str(linha['Jogo']).strip()

        # Insere ou atualiza os dados incluindo a nova posição do ranking
        cursor.execute('''
            INSERT OR REPLACE INTO jogos (
                id, jogo, genero, jogabilidade_nota, horas_semana, 
                idade_media, gasto_mensal_brl, fator_compra, 
                satisfacao, qtd_biblioteca_perfil, taxa_conclusao, posicao_ranking
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            int(linha['ID']),
            jogo_nome,
            linha['Genero'],
            linha['Jogabilidade_Nota'],
            linha['Horas_Semana'],
            linha['Idade_Media'],
            linha['Gasto_Mensal_BRL'],
            linha['Fator_Compra'],
            linha['Satisfacao'],
            linha['Qtd_Biblioteca_Perfil'],
            linha['Taxa_Conclusao'],
            int(linha['posicao_ranking'])
        ))
        
        jogo_id = int(linha['ID'])
        cursor.execute('DELETE FROM jogo_plataforma WHERE jogo_id = ?', (jogo_id,))

    conn.commit()
    conn.close()
    print("✨ Sucesso! Ranking gerado e 100 jogos importados com sucesso!")

if __name__ == "__main__":
    importar_e_ranquear_jogos()