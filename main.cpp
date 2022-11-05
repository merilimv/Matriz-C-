#include <iostream>
#include "./Classes/Metodos/Headers/GaussJacobi.h"
#include "./Classes/Metodos/Headers/gauss.h"
#include "./Classes/Metodos/Headers/GaussJordan.h"
#include "./Classes/Metodos/Headers/GaussSeidel.h"
#include "./Classes/Metodos/Headers/LU.h"

using namespace std;

int main(){
    Matrix m(3, 4);
    m.inputValue(0, 0, 6); m.inputValue(0, 1, 3); m.inputValue(0, 2, 1); m.inputValue(0, 3, 10);
    m.inputValue(1, 0, 4); m.inputValue(1, 1, 9); m.inputValue(1, 2, -3); m.inputValue(1, 3, 16);
    m.inputValue(2, 0, 1); m.inputValue(2, 1, -1); m.inputValue(2, 2, 3); m.inputValue(2, 3, 14);
    
    //eliminação de Gauss aparentemente funcionando
    //tá tendo aquela problema caso o valor seja MUITO próximo de 0
    //então quando o valor está em um limite tal, eu simplesmente aproximo pra 0
    //pensar em como fazer pra adicionar o vetor de respostas
    

    //implementar depois o teste para o critério de convergência do Gauss Jacobi
    GaussJacobi GJ(3);

    GJ.resolver(&m, 0.05);

    for(int i = 0; i < m.row; i++){
        cout << GJ.resposta[i] << '\n';
    }
}