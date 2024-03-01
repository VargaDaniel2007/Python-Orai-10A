def oraperc(ido: int):
    ora = ido // 60
    perc = ido - (60 * ora)
    
    return str(ora) + ' óra ' + str(perc) + ' perc'