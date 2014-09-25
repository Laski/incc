screenNum = 0;
res =[1280 1024];
clrdepth = 32;
[wPtr, rect]= Screen('OpenWindow', screenNum, 0, [0 0 res(1) res(2)], clrdepth);
black = BlackIndex(wPtr);
white = WhiteIndex(wPtr);
refresh = Screen('GetFlipInterval', wPtr);
HideCursor;
estimulos = [];
presiones = [];
tecla_presionada = false;  % Flag para no contar varias veces la misma presión de tecla.
i = 1;
inicio = GetSecs();
while length(presiones) < 11
    delta_inicio = GetSecs() - inicio;
    if length(estimulos) == 0 || delta_inicio > estimulos(length(estimulos)) + refresh*4
        % No fue mostrado ningún estímulo, o el último fue mostrado hace
        % suficiente tiempo. Pinto todo de blanco.
        Screen('FillRect', wPtr, white);
        Screen('Flip', wPtr);
    end
    if delta_inicio >= i*0.9
        % Toca mostrar un estímulo
        Screen('FillOval', wPtr, black, [500 350 650 450]);
        t_estimulo = Screen('Flip', wPtr);
        delta_estimulo = t_estimulo - inicio;
        estimulos = [estimulos delta_estimulo];
        i = i+1;
    end
    [isDown, t_presion, keyCode, deltaSecs] = KbCheck();
    if isDown & not(tecla_presionada)
        % Hay una telca presionada y no había ninguna presionada hace
        % instantes.
        delta_presion = t_presion - inicio;
        presiones = [presiones delta_presion];
        tecla_presionada = true;    % Prendo el flag
    end
    if not(isDown)
        % Ya no hay tecla presionada, apago el flag
        tecla_presionada = false;
    end
end
resultados = [];
for i = 1:length(presiones)
    % Comparo cada presión con su estímulo correspondiente
    if i > length(estimulos)
        break
    end
    resultados = [resultados presiones(i)-estimulos(i)];
end
resultados % Muestro resultados
Screen('CloseAll');
ShowCursor;
