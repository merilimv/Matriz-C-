#pragma once
#include "../../ClassMatriz/ClassMatriz.h"

class MetodoNumerico {
    public:
    vector<double> resposta;

    MetodoNumerico(int n);

    int transformar(const Matrix& m);

    int resolver(const Matrix& m);
    
};