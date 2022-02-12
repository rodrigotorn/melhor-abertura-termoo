import pandas as pd

dicio = pd.read_csv('dicio', header=None)
dicio.columns = ['palavras']

dicio['qt_letras'] = dicio['palavras'].str.len()
dicio = dicio[dicio['qt_letras'] == 5]
dicio.reset_index(drop=True, inplace=True)
dicio.drop(columns='qt_letras', inplace=True)

char_especiais = ['à', 'á', 'â', 'ã', 'ç', 'é',
  'ê', 'í', 'ï', 'ó', 'ô', 'õ', 'ú']
char_substitutos = ['a', 'a', 'a', 'a', 'c', 'e',
  'e', 'i', 'i', 'o', 'o', 'o', 'u']

for esp, sub in zip(char_especiais, char_substitutos):
  dicio['palavras'] = dicio['palavras'] \
    .str.replace(esp, sub)
    
dicio.drop_duplicates(inplace=True)

dicio.to_csv('palavras_possiveis.txt',
  header=False,
  index=False
)
