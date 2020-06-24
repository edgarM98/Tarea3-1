# Tarea 3
## María Paula Ruiz, B76878

 ## Funciones de densidad marginales
 Para los datos en X y en Y se obtuvo que la curva de mejor ajuste es una distribución gaussiana, donde las funciones de densidad están dadas por las siguientes ecuaciones: 
 
 $$ f_x(x) = \frac{1}{\sigma \sqrt{2\pi}} \cdot e^{-\frac{(x-\mu)^2}{2\sigma^2}} $$
 $$ f_y(y) = \frac{1}{\sigma \sqrt{2\pi}} \cdot e^{-\frac{(y-\mu)^2}{2\sigma^2}} $$
donde los valores de X están entre 5 y 10 y los valores de Y entre 5 y 25. Para encontrar los valores de la función de densidad marginal para ambas variables se realizó una sumatoria de los valores de probabilidad relacionados a cada una de las variables. Con los datos se estas sumatorias, se graficaron la funciones de densidad marginales para X y Y sin curvas de ajuste. La gráfica para la función de densidad marginal de X es:

![Gráfica para la función de densidad marginal de X.](/DensidadX.png)

La gráfica para la función de densidad marginal de Y es: 
![Marginal Y](https://lh3.googleusercontent.com/DbA3YpGchIYrI0R_T9X3QxgtrDzBBrp-opOGb-Q92Z3JAshNGELkmBZVAIqdQm9kijTlaUBqu7pY "Y")

Para ambas se encontró que la curva de mejor ajuste es gaussiana, con esto fue posible graficar las curvas de mejor ajuste. La curva de mejor ajuste obtenida para X es: 
![enter image description here](https://lh3.googleusercontent.com/Qgxb-__enzDLdWfJ5r7-90sh2Fh1ax-8Lrf9gZrZZMMs8Z5ko7yfZ4-EY8csBxASDJ6C-ftUDhhy "ajusteX")

 La curva de mejor ajuste obtenida para Y es: 
 ![enter image description here](https://lh3.googleusercontent.com/LaLt8jwDQ3KUqRMNCytmAzB8C_wu66KTJRIC6sHxSNv_d6xO4_2qKSmqBA67c3P4jbTPdUu7iKW0 "ajusteY")

Como se observa en las siguientes gráficas donde se graficaron ambas curvas, con y sin ajuste, las curvas de ajuste son adecuadas para modelar los datos: 

 - X: 
 ![](https://lh3.googleusercontent.com/5XQtopYOoPsJYh7ErfF82O-TEuS54uTdbhZAKwpND89zOL8C61z0Ws7ljNDVOW2e4w8Yg3lhKFpx "ambasX")
 
 - Y: 
 ![Y](https://lh3.googleusercontent.com/nKpNYZr4l3uPKCqI4k2ApuHtvXYRoTBpZgasiaQRVMPfrMn7_jbHiQ6tt0jpTMss-ynRv0Mv_h7M "ambasY")
Con este modelado fue también posible encontrar los valores de los parámetros $\mu_x$, $\sigma_x$, $\mu_y$ y $\sigma_y$. Se obtuvieron los siguientes resultados: 
 - $\mu_x$ = 9.90484381
 - $\sigma_x$ = 3.29944286
 - $\mu_y$ = 15.0794609
 - $\sigma_y$ = 6.02693775

## Función de densidad conjunta
Como se asume la independencia estadística de las variables, se tiene que la función de densidad conjunta es: 
$$ f_{x,y}(x,y) = f_x(x)\cdot f_y(y)$$
Considerando que ya previamente se había encontrado la expresión para ambas funciones de densidad marginal, se tiene que la expresión para la función de densidad conjunta es: 
$$ f_{x,y}(x,y) = (\frac{1}{\sigma \sqrt{2\pi}} \cdot e^{-\frac{(x-\mu)^2}{2\sigma^2}} ) \cdot (\frac{1}{\sigma \sqrt{2\pi}} \cdot e^{-\frac{(y-\mu)^2}{2\sigma^2}})  $$
Simplificando esta expresión se obtiene: 
$$ f_{x,y}(x,y) = \frac{e^{-\frac{(x-\mu_x)^2}{2\sigma_x^2}-{\frac{(y-\mu_y)^2}{2\sigma_y^2}}}}{2\pi\sigma_x\sigma_y} $$

Donde los valores para las variables $\mu_x$, $\sigma_x$, $\mu_y$ y $\sigma_y$ fueron encontrados previamente. 
Al graficar esto se obtiene la siguiente gráfica en 3D: 

![xy3D](https://lh3.googleusercontent.com/mVWvl1BsvTqTeCtfQbyAZWxSEtY8TPhGZtYuU-EprGKyVlGtikscZ_tkYHOsLL-lTq5Xa9mm9RMA "3d")

## Correlación, covarianza y coeficiente de correlación
Para el cálculo de la correlación se usó la siguiente fórmula: 
$$ \sum_{y=5}^{25}\sum_{x=5}^{15}xy f_{x,y}(x,y)$$
El resultado obtenido fue: 149.54281.
Al realizar el cálculo para E[X]*E[Y] se obtuvo que esto es: 149.4840485.
Como se observa es posible aproximar la correlación con esta multiplicación, lo que directamente implica que no hay correlación. Esto hubiera sido posible concluirlo desde el inicio puesto que se estaba asumiendo que las variables son independientes y todas las variables independientes no tienen correlación. 

Para el cálculo de la covarianza se usó la siguiente fórmula: 
$$ \sum_{y=5}^{25}\sum_{x=5}^{15}(x-\bar{X})(y-\bar{Y}) f_{x,y}(x,y)$$
El resultado obtenido fue 0.06669156988. Este valor fue el esperado, puesto que cuando dos variables no tienen correlación, se espera que su covarianza sea 0, y se observa que en efecto el resultado obtenido es un número muy pequeño que se puede aproximar a 0. 

Para el cálculo del coeficiente de correlación se usó la siguiente fórmula: 
$$ \sum_{y=5}^{25}\sum_{x=5}^{15}\frac{(x-\bar{X})}{\sigma_x}\frac{(y-\bar{Y})}{\sigma_y} f_{x,y}(x,y)$$
El resultado obtenido fue: 0.00335377268. Al igual que con la covarianza, debido a la independencia estadística de las variables se espera que este coeficiente tenga un valor de 0, y en efecto, se obtuvo un valor muy pequeño, que igualmente se puede aproximar a 0. 
