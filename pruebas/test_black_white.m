screenNum = 0;
res =[1280 1024];
clrdepth = 32;
[wPtr, rect]= Screen('OpenWindow', screenNum, 0, [0 0 res(1) res(2)], clrdepth);
black = BlackIndex(wPtr);
white = WhiteIndex(wPtr);
Screen('FillRect', wPtr, black);
Screen(wPtr, 'Flip');
HideCursor;
tic
while toc < 3
    ;
end
Screen('FillRect', wPtr, white);
Screen(wPtr, 'Flip');
HideCursor;
tic
while toc < 3
    ;
end
Screen('CloseAll');
ShowCursor;

