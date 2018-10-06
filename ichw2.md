1、因为计算机逻辑体系也是一个形式系统，必定包含某些系统内所允许的方法既不能证明真也不能证伪的命题。  
2、证明方法是反证法。假设有一算法f（program, input），如果程序对输入会停机则输出true，反之输出false。构造一个程序g(program)，若f(program, program)输出true则g(program)不会停机，若f(program, program)输出false则g(program)会停机。当调用g（g）时，若f（program, input）判定其会停机则输出true，那么其又不会停机；若f（program, input）判定其不会停机则输出false，其又会停机，两种结果都是矛盾的  
3、数学原理：哥德尔不完全性定理，即任意一个包含一阶谓词逻辑与初等数论的形式系统，都存在一个命题，它在这个系统中既不能被证明为真，也不能被证明为否。
