import os
from pathlib import Path


def create_catalogs(tbl, now):
    """
    create_catalogs [создание каталогов]
    [создание каталога, куда сохраняются скриншоты]
    Args:
        tbl ([string]): [alias name folder]
    Returns:
        [list]: [folder path and datetime]
    """
    
    #работа с каталогами
    
    path = os.path.dirname(os.getcwd())

    #необходимые пути
    parent = path+'/'+tbl
    folder = parent+'/'+now

    #если нет каталога, то создаем
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    return folder
