    deslocamento = max(df_roubo_veiculo_out_sup['roubo_veiculo']) * 0.02

    for i, valor in enumerate(df_roubo_veiculo_out_sup['roubo_veiculo']):
        plt.text(
            i, # x
            valor + deslocamento, # y
            f'{valor:,}',
            ha='center'
        )

    
        

    
        
        

        
    
    
