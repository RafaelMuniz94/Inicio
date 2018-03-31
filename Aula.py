class Aula:
    def __init__(self,materia,serie):
        self.materia = materia
        self.serie = serie

    def retorna_Aulas(self):
        return 'Matéria: {} \n Série: {}'.format(self.materia,self.serie)