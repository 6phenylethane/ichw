1、因为计算机逻辑体系也是一个形式系统，必定包含某些系统内所允许的方法既不能证明真也不能证伪的命题。  
2、证明方法是反证法。假设有一算法f（program, input），如果程序对输入会停机则输出true，反之输出false。构造一个程序g(program)，若f(program, program)输出true则g(program)不会停机，若f(program, program)输出false则g(program)会停机。当调用g（g）时，若f（program, input）判定其会停机则输出true，那么其又不会停机；若f（program, input）判定其不会停机则输出false，其又会停机，两种结果都是矛盾的  
3、数学原理：哥德尔不完全性定理，即任意一个包含一阶谓词逻辑与初等数论的形式系统，都存在一个命题，它在这个系统中既不能被证明为真，也不能被证明为否。  
补码：计算机中使用二进制，而每个十进制整数都能转换为一个二进制数，正数的补码即为对应的二进制数本身，负数的补码要先忽略符号转换为二进制，再每位数字取反（0变成1,1变成0）后整体加1。计算机计数还有原码和反码，原码就是除了第一位数字表示符号以外，其余位数的二进制数表示一个十进制整数，根据码位数的需要，在前边的所有空位补上0；而反码不用额外的符号位，将一个正整数的原码所有位数取反即为该正整数的相反数。计算机计算追求简便，而原码和反码在运算过程中需要进一步处理，比较麻烦，且都存在两个码表示0，而补码运算简便，不仅0只有一种表示方式，而且加法和减法都能直接用补码进行运算，所得补码结果转换为整数即为运算结果，即[X+Y]补 = [X]补 + [Y]补，[X-Y]补 = [X]补 - [Y]补 = [X]补 + [-Y]补。  
  
浮点数  
      
| sign | exp  | frac     | value |
|---|---|---|---|
| * | 0000 | 000 0000 |  +-0  |
| * | 0111 | 000 0000 | +-1.0 |
| * | 0000 | 111 1111 | +-(1-2^-7)*2^-7  最大和最小非规范数 |
| * | 0000 | 000 0001 | +-1*2^-14 |
| * | 1110 | 111 1111 | +-2*2^7 (最大和最小规范化浮点数) |
| * | 1111 | 000 0000 | 正负无穷大 |
| * | 1111 |  不全是0 |   NaN |
