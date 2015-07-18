from recipe import Recipe
from ingredient import IngredientRecette
from __builtin__ import raw_input
from exception import MyException


class ConsoleView:
    """Console view of the application"""
    
    def __init__(self, iModel):
        self.__model = iModel
    
    def run(self):
        aExit = False
        print("Escolhe o que quer fazer:")
        print("1 - Calcular peso de uma porcao de uma receita.")
        print("2 - Reiniciar os ingredientes.")
        print("3 - Sair.")
        while(not aExit):
            aChoix = raw_input("Opcao: ")
            try:                                # Test if it is an number
                aChoix = int(aChoix)
                if aChoix > 0 and aChoix < 4:   # Test if this number belongs to one choice
                    pass
                else: 
                    print("Por favor, escolher em {1, 2, 3}.")
                    continue
            except:
                print("Por favor, entrar um numero.") 
                continue
            
            if aChoix == 1 :    # Calculate portion
                self.__enterRecipe()
                self.__displayResult(self.__model.calculatePortions())
            elif aChoix == 2:   # Reset local database
                self.__model.resetDatabase()
            elif aChoix == 3:   # Exit
                aExit = True
            else:
                raise MyException("run: opcao impossivel.\n")
    
    def __displayResult(self, iResults):
        for aResult in iResults :
            print(aResult)
  
    def __enterRecipe(self):
        """Procedure to set a new recipe"""
        
        aNiveau = 0; aListIngr=[]   # Meta Group level of the recipe and ingredients list
        aCheckpoint = False         # Boolean used to check the input type 
        
        # Set o recipe level
        print("Entrar o nivel da receita :")
        while(not aCheckpoint):
            aNiveau = raw_input("Nivel: ")
            try:                                # Test if it is an number
                aNiveau = int(aNiveau)
                if aNiveau > 0 and aNiveau < 5: # Test if this number is a MetaGroup level
                    aCheckpoint = True
                else: print("Por favor, escolher em {1, 2, 3, 4}.")
            except:
                print("Por favor, entrar um numero.") 
                continue
        
        # Set ingredients and their weight of the recipe        
        aCheckpoint = False         # Used to finish ingredient set
        aIdx = 0                    # Added ingredient index
        aNumero=0; aIngredient=0    # Ingredient number, ingredient object in the recipe
        aPoids=0;                   # Ingredient weight in the recipe
        aDeadWeight=0;              # Weight of ingredients without energetic value
        
        aCheckpointIngr = False
        
        print("Entra o peso dos ingredientes sem valor energetico :")
        # Set weight of ingredients without energetic value
        while(not aCheckpointIngr):
            aPeso = raw_input("Peso: ")
            try:                                                    
                aPeso = int(aPeso)      # Test if it is an number
                aDeadWeight = aPeso     # set dead weight
                aCheckpointIngr = True
            except:
                print("Por favor, entrar um numero.") 
        
        aCheckpointIngr = False
        
        print("Entrar os ingredientes et os pesos de cada:")
        while(not aCheckpoint):
            # Set ingredient
            while(not aCheckpointIngr):
                print("Entrar o numero do ingrediente "+str(aIdx+1)+": ")
                aNumero = raw_input("Numero: ")
                try:                                                        # Test if it is an number
                    aNumero = int(aNumero)
                    if self.__model.checkNumIngr(aNumero):                  # Test if the ingredient number exist
                        aIngredient = self.__model.getIngredient(aNumero)   # Set choosen ingredient
                        aCheckpointIngr = True
                    else: print("Por favor, escolher um numero valido.")
                except:
                    print("Por favor, entrar um numero.") 
                
            aCheckpointIngr = False
            
            # Set weight
            while(not aCheckpointIngr):
                print("Entrar o peso em g. do ingrediente "+str(aIdx+1)+": ")
                aPoids = raw_input("Peso: ")
                try:                        # Test if it is an number
                    aPoids = int(aPoids)
                    aCheckpointIngr = True
                except:
                    print("Por favor, entrar um numero.")
                    
            # Append to the ingredient recipe list
            aListIngr.append(IngredientRecette(aPoids, aIngredient)) 
            
            # Add another ingredient ?
            aCheckpointIngr = False; aChoix = 0;
            while(not aCheckpointIngr):
                print("Quer adicionar um outro ingrediente ? (s/n)")
                aChoix = raw_input("s ou n ? ")
                if aChoix == "s" :          # Check if the response is "s"
                    aCheckpointIngr = True
                    aIdx += 1
                elif aChoix == "n" :        # Check if the response is "n"
                    aCheckpointIngr = True
                    aCheckpoint = True
                    self.__model.recette = Recipe(aNiveau, aListIngr, aDeadWeight)
                else:
                    print("Por favor, entrar s ou n.")
                    
            aCheckpointIngr = False

                    
            
            
        