高速缓冲存储器的结构和作用原理  
  
高速缓冲存储器是存在于主存与CPU之间的一级存储器，一般L1cache集成在cpu内，L2cache集成在主板上，主要由静态存储芯片(SRAM)组成  
工作原理：由于cpu的存储速度非常快而存储空间非常小，主存储器的存储速度慢而存储空间大，这两者在进行数据传输的时候，需要一个起到桥梁作用的存储器，这就是高速缓冲存储器cache。cpu在读取数据时，只读取cache上的数据，若读取成功，则能大大提高运算速度，若读取未成功，会到内存中复制需要的数据块, 覆盖cache的内容然后读取数据，这样比直接读取主存储器上的数据快得多
